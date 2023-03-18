# from zipfile import *
# f=ZipFile("files.zip",'w',ZIP_DEFLATED)
# f.write("abc.txt")
# f.write("first.py")
# # f.write("file2.txt")
# # f.write("file3.txt")
# f.close()
# print("files.zip file created successfully")

# import os
# cwd=os.getcwd()
# print("Current Working Directory:",cwd)


# import os
# os.mkdir("mysub")
# print("mysub directory created in cwd")

# import os
# os.mkdir( "mysub/mysub2")
# print("mysub2 created inside mysub")

# import os
# os.mkdir( "mysub/mysub2/mysub3")
# print("mysub2 created inside mysub")


# Q5. To remove a directory:
# import os
# os.rmdir("mysub/mysub2/mysub3")
# print("mysub2 directory deleted")


# import os
# os.rename("mysub","newdir")
# print("mysub directory renamed to newdir")


import os
print(os.listdir("."))