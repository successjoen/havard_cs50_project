def application():
    file = input("file name: ").strip().lower()
    if file.endswith("jpeg")or file.endswith("jpg"):
        print("image/jpeg")
    elif file.endswith("png"):
        print("image/png")
    elif file.endswith("gif"):
        print("image/gif")
    elif file.endswith("pdf"):
        print("application/pdf")
    elif file.endswith("txt"):
        print("text/plain")
    elif file.endswith("zip"):
        print("application/zip")
    else:
        print("application/octet-stream")

if __name__ == "__main__":
    application()
