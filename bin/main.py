from src.endpoint.iot_endpoint_server import IoTEndpointServer
import argparse


def main():
    """
    Main function of the program.
    This function parses all arguments and starts the WebSocket server.
    """
    # Parse all CLI arguments
    parser = argparse.ArgumentParser(description="IoT-Utilities Python Example Server")
    parser.add_argument("--port", action="store", type=int, help="Port of the WebSocket server")
    parser.add_argument("--certificate", action="store", type=str, help="Path of the SSL certificate file")
    parser.add_argument("--raw", action="store_true", help="Enables/disables raw protobuf message output")
    arguments = parser.parse_args()

    # Configure and start the WebSocket server
    server = IoTEndpointServer(
        arguments.port if arguments.port else 5443,
        arguments.certificate,
        arguments.raw
    )
    server.start()


if __name__ == "__main__":
    main()
