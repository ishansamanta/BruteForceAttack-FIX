 def secret_language(password):
            """Encode a message by reversing it and adding secret padding"""
            reversed_msg = password[::-1]
            encoded_msg = "@347648^haj#hag^kol*ihardfhsecu785roamapple" + reversed_msg + "fire94347fiewr53325igreatfhefhifhefhf8helpf3r8hfnapplemohwicsi"
            return encoded_msg
