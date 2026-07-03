admins = ["alice", "bob", "charlie"]
user = "ALICE"

if (
    user.lower() in admins == True
):  # chain behaves strange because of double evaluation, remove == True for the fix
    print("Access Granted")
else:
    print("Access Denied")
