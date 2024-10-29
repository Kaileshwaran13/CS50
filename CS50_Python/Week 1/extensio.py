f_name = input("File name: ")
f_name = f_name.lower()
f_name = f_name.strip()
f_name = f_name.split(".")
if(f_name[-1] == "gif"):
    print("image/gif")
elif (f_name[-1] == "jpg" or f_name[-1] == "jpeg"):
    print("image/jpeg")
elif (f_name[-1] == "png"):
    print("image/png")
elif (f_name[-1] == "pdf"):
    print("application/pdf")
elif (f_name[-1] == "txt"):
    print("text/plain")
elif (f_name[-1] == "zip"):
    print("application/zip")
else:
    print("application/octet-stream")