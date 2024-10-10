import os
class Utils:

    @staticmethod
    def pointer():
        return ">"


    # home path
    @staticmethod
    def get_home_path():
        # gets user $home director
        def get_home_directory_with_expanduser():
            return os.path.expanduser("~")
        home_dir = get_home_directory_with_expanduser()
        return home_dir
    # end home path
