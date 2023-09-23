print(open("name.dat").readlines()[0])
password = input("Password: ")
if password == open("password.dat").readlines()[0]:
    import boot.osm as osm