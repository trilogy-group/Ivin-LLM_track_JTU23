import os
import openai
import pkg_resources

def main():
    version = pkg_resources.get_distribution("openai").version
    print("OpenAI version:", version)
    # Additional code to test OpenAI functionality

if __name__ == '__main__':
    main()

