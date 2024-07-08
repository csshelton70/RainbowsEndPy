""" Main entry point for the program """
import argparse
import game
import logging

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')  
logger = logging.getLogger(__name__)
_game = game.Game()

parser = argparse.ArgumentParser()
if ( _game.exists() == False ):
    parser.add_argument("-ng","--newgame",action="store_true", help="Starts a new game if there is not one in progress")

parser.add_argument("-pt","--processturn",action="store_true", help="process the next turn of the game")
parser.add_argument("-i","--info",action="store_true", help="display information about the game")
# --adduser <username>
parser.add_argument("-au","--adduser", help="Only available before the game beings.  Add a new user to the list")


args = parser.parse_args()

if ( args.newgame == True):
    game1 = game.Game()
    game1.create_new_game();
elif ( args.processturn == True):
    x="x"
elif ( args.info == True ):
    x="x"
elif ( args.adduser != None ):
    x=args.adduser
else:
    x="x"



# class REFrame(wx.Frame):
#     """ Windows """   
#     def __init__(self):
#         super().__init__(parent=None, title='Rainbow\'s End')
        
#         # Add a panel and expand it to fill the frame
#         self.panel = wx.Panel(self)
#         frame_sizer = wx.BoxSizer(wx.VERTICAL)
#         frame_sizer.Add(self.panel,1,wx.ALL|wx.EXPAND)

#         # Add a multi-line text control to panel and expand it to fit
#         panel_sizer = wx.BoxSizer(wx.VERTICAL)  
#         self.panel.SetSizer(panel_sizer)
#         self.panel.my_text = wx.TextCtrl(self.panel, style=wx.TE_MULTILINE)
#         font1 = wx.Font(10, wx.MODERN, wx.NORMAL, wx.NORMAL, False, u'Consolas')
#         self.panel.my_text.SetFont(font1)
#         panel_sizer.Add(self.panel.my_text, 1, wx.ALL|wx.EXPAND)

#         self.panel.Show()

#         self.create_menu()
#         self.Show()
#         self.Maximize()

#     def create_menu(self):
#         menu_bar = wx.MenuBar()

#         file_menu = wx.Menu()
#         help_menu = wx.Menu()

#         game1 = game.Game();
#         if ( game1.in_progress() == False):  
#             new_game_menu_item = file_menu.Append(wx.ID_ANY, "&New Game", "Create a new game")
#         else:
#             check_email_menu_item = file_menu.Append(wx.ID_ANY, "&Check Email", "Cheack email for data")
            
#         run_turn_menu_item = file_menu.Append(wx.ID_ANY,"&Run Turn","Process files and generate turn data")
#         show_map_menu_item = file_menu.Append(wx.ID_ANY,"&Show Map","Show map from current turn")        
#         split_menu_item = file_menu.AppendSeparator()
#         exit_app_menu_item = file_menu.Append( wx.ID_EXIT, "E&xit","Exit App" )

#         readme_menu_item = help_menu.Append(wx.ID_ANY,"&About","About the game")
#         rules_menu_itesm = help_menu.Append(wx.ID_ADD,"&Rules","View game Rules")
#         history_menu_item = help_menu.Append(wx.ID_ANY, "History","View history" )
#         license_menu_item = help_menu.Append(wx.ID_ANY,"&License","View License")

#         menu_bar.Append(file_menu, "&File")
#         menu_bar.Append(help_menu, "&Help")

#         #Bind all the menu events
#         #self.Bind(event, handler, sources)
#      #   if ( new_game_menu_item != Null):   
#      #       self.Bind(wx.EVT_MENU, self.on_new_game, new_game_menu_item)
#         self.Bind(wx.EVT_MENU, self.on_run_Turn, run_turn_menu_item)
#         self.Bind(wx.EVT_MENU, self.on_show_map, show_map_menu_item)
#         self.Bind(wx.EVT_MENU, self.on_exit, exit_app_menu_item)
#         self.Bind(wx.EVT_MENU, self.on_show_readme, readme_menu_item)
#         self.Bind(wx.EVT_MENU, self.on_show_rules, rules_menu_itesm)
#         self.Bind(wx.EVT_MENU, self.on_show_history, history_menu_item)
#         self.Bind(wx.EVT_MENU, self.on_show_license, license_menu_item)

#         # Create the status Bar
#         self.SetMenuBar(menu_bar)
#         self.statusBar = self.CreateStatusBar(2)
#         self.statusBar.SetStatusText("Welcome")

#     def load_file(self,filename):
#         self.panel.my_text.Clear()
#         if os.path.exists(filename):
#             with open(filename) as fobj:
#                 for line in fobj:
#                     self.panel.my_text.WriteText(line)

#     #Create all the events that are bound to menu items    
#     def on_exit(self, e):
#         self.Close()

#     def on_new_game(self,e):
#         game1 = game.Game()
#         game1.create_new_game()
#         return

#     def on_run_Turn(self,e):
#         wx.MessageBox('Run Turn', 'Menu Selection', wx.OK)
#         return

#     def on_show_map(self,e):
#         wx.MessageBox('Show Map', 'Menu Selection', wx.OK)
#         return

#     def on_show_readme(self,e):
#         wx.MessageBox('Show ReadMe', 'Menu Selection', wx.OK)
#         return

#     def on_show_rules(self,e):
#         self.load_file(".\\rules.txt")
#         return

#     def on_show_license(self,e):
#         self.load_file(".\\LICENSE")
#         return

#     def on_show_history(self,e):
#         self.load_file(".\\history.txt")
#         return

# if __name__ == '__main__':
#     app = wx.App()
#     frame = REFrame()
#     app.MainLoop()
