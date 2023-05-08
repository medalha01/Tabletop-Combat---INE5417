import logging
from VirtualTableTop.game_logic.visual_interface.InterfaceUser import InterfaceUser

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    logging.getLogger("__main__.py").info("Project has run")
    # Add your logic here

    Interface = InterfaceUser()
    Interface.main()
