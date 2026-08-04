from app.services.llm_service import generate_response


def main():
    reply = generate_response("Say hello in one sentence.")
    print(reply)


if __name__ == "__main__":
    main()