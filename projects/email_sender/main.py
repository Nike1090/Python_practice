import sys 

sys.path.insert(1, 'C:\\Users\\nike9\\OneDrive\\Python practice\\lvl_intermediate')
import mail

if __name__ == "__main__":
    email_message = mail.build_the_message(
        "Hello!",
        """
        Hello vikram,
        How are you doing?
        Thanks       
        """
    )
    mail.send(email_message)