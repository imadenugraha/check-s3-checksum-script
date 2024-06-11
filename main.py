import argparse

from check_s3_checksum.upload_object import upload_object


def main():
    parser = argparse.ArgumentParser(description='Upload object to S3')
    parser.add_argument("-f", "--file", help="full path of file or file name",
                        required=True, type=str)
    parser.add_argument("-k", "--key", help="full name or path object on bucket",
                        required=True, type=str)
    args = parser.parse_args()

    upload_object(args.file, args.key)


if __name__ == "__main__":
    main()
