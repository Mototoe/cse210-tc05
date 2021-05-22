class Jumper:
    """The Jumper class"""

    def get_parachute(self, lives):
        """Draw Jumper and subtract Lines for loss of life"""

        message_1 = (" __ \n" +
                     "/__\ \n" +
                     "\  / \n" +
                     " \/ \n" +
                     "  0 \n" +
                     " /|\ \n" +
                     " / \ \n" +
                     "\n" +
                     "^^^^^^^^ \n")
        message_2 = ("/__\ \n" +
                     "\  / \n" +
                     " \/ \n" +
                     "  0 \n" +
                     " /|\ \n" +
                     " / \ \n" +
                     "\n" +
                     "^^^^^^^^ \n")
        message_3 = ("\  / \n" +
                     " \/ \n" +
                     "  0 \n" +
                     " /|\ \n" +
                     " / \ \n" +
                     "\n" +
                     "^^^^^^^^ \n")
        message_4 = (" \/ \n" +
                     "  0 \n" +
                     " /|\ \n" +
                     " / \ \n" +
                     "\n" +
                     "^^^^^^^^ \n")
        message_5 = ("  X \n" +
                     " /|\ \n" +
                     " / \ \n" +
                     "\n" +
                     "^^^^^^^^ \n")

        if lives == 4:
            return message_1
        elif lives == 3:
            return message_2
        elif lives == 2:
            return message_3
        elif lives == 1:
            return message_4
        else:
            return message_5
