from .cli import main

if __name__ == "__main__":
    try:
        print("Welcome to PlumbBagel! Starting up...")
        main()
    except KeyboardInterrupt:
        print("\nGoodbye! Shutting down.")
