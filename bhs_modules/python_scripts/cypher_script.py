import argparse
from useful_functions import process_message


def main():
    parser = argparse.ArgumentParser(
        description="Encrypt or decrypt a text file using a unicode Vigenere-style cipher."
    )

    parser.add_argument(
        "-i",
        "--input",
        required=True,
        help="Path to the input text file."
    )

    parser.add_argument(
        "-o",
        "--output",
        required=True,
        help="Path to the output text file."
    )

    parser.add_argument(
        "-k",
        "--key",
        required=True,
        help="Secret key used for encryption or decryption."
    )

    parser.add_argument(
        "-m",
        "--mode",
        required=True,
        choices=["encryption", "decryption"],
        help="Mode: encryption or decryption."
    )

    args = parser.parse_args()

    with open(args.input, "r", encoding="utf-8") as f:
        message = f.read()

    encrypt = args.mode == "encryption"
    processed_message = process_message(message, args.key, encrypt=encrypt)

    with open(args.output, "w", encoding="utf-8") as f:
        f.write(processed_message)

    print(f"Done! Saved result to {args.output}")


if __name__ == "__main__":
    main()