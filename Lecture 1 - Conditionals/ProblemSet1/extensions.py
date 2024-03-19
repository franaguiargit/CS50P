name_of_file = input("File name: ").lower()

match name_of_file:
    case _ if name_of_file.endswith('.gif'):
        print("image/gif")
    case _ if name_of_file.endswith('.jpg'):
        print("image/jpg")
    case _ if name_of_file.endswith('.jpeg'):
        print("image/jpeg")
    case _ if name_of_file.endswith('.png'):
        print("image/png")
    case _ if name_of_file.endswith('.pdf'):
        print("application/pdf")
    case _ if name_of_file.endswith('.txt'):
        print("text/plain")
    case _ if name_of_file.endswith('.zip'):
        print("application/zip")
    case _:
        print("application/octet-stream")  # Default case for unrecognized suffixes
