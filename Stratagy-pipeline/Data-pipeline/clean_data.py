

class CleanFinData:
    """
    Deal with outliers and N.A. values and any other cleaning that
    has to be done. Get data from get_data -> Then feed into label_data
    """

    def __init__(self):
        self.data = []