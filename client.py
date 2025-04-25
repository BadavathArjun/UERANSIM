import grpc
import newsfeed_pb2
import newsfeed_pb2_grpc

def run():
    channel = grpc.insecure_channel('localhost:50051')
    stub = newsfeed_pb2_grpc.NewsFeedServiceStub(channel)

    # Post a message
    user = input("Enter your name: ")
    message = input("Enter your message: ")
    response = stub.PostMessage(newsfeed_pb2.PostRequest(user=user, message=message))
    print(response.status)

    # Get all messages
    all_messages = stub.GetMessages(newsfeed_pb2.Empty())
    print("\n--- All Messages ---")
    for msg in all_messages.messages:
        print(f"{msg.user}: {msg.message}")

if __name__ == '__main__':
    run()
