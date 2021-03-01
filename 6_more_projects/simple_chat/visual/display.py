
class Display:

    @staticmethod
    def display_message_list(msg_list, is_inbox):
        """
        msg_list is a list of ChatMessage object
        Columns
            Number (8)
            Date (15)
            Sender (15)
            Message (30)
        """
        header = "-" * 73
        user_col = "Sender" if is_inbox else "Recipient"
        banner = "|{}|{}|{}|{}|".format(
            str.center("Number", 8),
            str.center("Date", 15),
            str.center(user_col, 15),
            str.center("Message", 30)
        )

        print(header)
        print(banner)
        print(header)

        item_number = 1
        for msg in msg_list:
            str_date = str(msg.date)
            str_msg = msg.message

            if len(str_msg) >= 26:
                str_msg = str_msg[0:25] + "..."

            str_date = str_date[0: str_date.index(' ')]
            user_col = msg.sender if is_inbox else msg.recipient

            msg_output = "|{}|{}|{}|{}|".format(
                str.center(str(item_number), 8),
                str.ljust(str_date, 15),
                str.ljust(user_col, 15),
                str.ljust(str_msg, 30)
            )
            print(msg_output)
            item_number += 1

        print(header)

    @staticmethod
    def display_message(msg):
        """
        msg is a ChatMessage object
        """
        header = "-" * 73

        print(header)
        print("{}: {}".format(str.ljust("Date", 20), str(msg.date)))
        print("{}: {}".format(str.ljust("Sender", 20), msg.sender))
        print("{}: {}".format(str.ljust("Recipient", 20), msg.recipient))
        print("{}: {}".format(str.ljust("Read", 20), msg.read))
        print("{}:".format(str.ljust("Message", 20)))
        print("\n{}".format(msg.message))
        print(header)
