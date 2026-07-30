from app.auth.hashing import hash_password, verify_password

password = "mypassword123"

hashed = hash_password(password)

print(f"Generated Hash: {hashed}")
print(f"Correct Password: {verify_password(password, hashed)}")
print(f"Wrong Password: {verify_password('wrongpassword', hashed)}")