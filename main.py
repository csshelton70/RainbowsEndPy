""" Main entry point for the program """
import wx


class REFrame(wx.Frame):
    """ Windows """   
    def __init__(self):
        super().__init__(parent=None, title='Rainbow\'s End')
        panel = wx.Panel(self)        
        my_sizer = wx.BoxSizer(wx.VERTICAL)  
        panel.SetSizer(my_sizer)
        self.create_menu()
        self.Show()

    def create_menu(self):
        menu_bar = wx.MenuBar()

        file_menu = wx.Menu()
        help_menu = wx.Menu()

        new_game_menu_item = file_menu.Append(wx.ID_ANY, "&New Game", "Create a new game")
        run_turn_menu_item = file_menu.Append(wx.ID_ANY,"&Run Turn","Process files and generate turn data")
        show_map_menu_item = file_menu.Append(wx.ID_ANY,"&Show Map","Show map from current turn")        
        split_menu_item = file_menu.AppendSeparator()
        exit_app_menu_item = file_menu.Append( wx.ID_EXIT, "E&xit","Exit App" )

        readme_menu_item = help_menu.Append(wx.ID_ANY,"&About","About the game")
        rules_menu_itesm = help_menu.Append(wx.ID_ADD,"&Rules","View game Rules")
        history_menu_item = help_menu.Append(wx.ID_ANY, "History","View history" )
        license_menu_item = help_menu.Append(wx.ID_ANY,"&License","View License")

        menu_bar.Append(file_menu, "&File")
        menu_bar.Append(help_menu, "&Help")

        #Bind all the menu events
        #self.Bind(event, handler, sources)
        self.Bind(wx.EVT_MENU, self.on_new_game, new_game_menu_item)
        self.Bind(wx.EVT_MENU, self.on_run_Turn, run_turn_menu_item)
        self.Bind(wx.EVT_MENU, self.on_show_map, show_map_menu_item)
        self.Bind(wx.EVT_MENU, self.on_exit, exit_app_menu_item)
        self.Bind(wx.EVT_MENU, self.on_show_readme, readme_menu_item)
        self.Bind(wx.EVT_MENU, self.on_show_rules, rules_menu_itesm)
        self.Bind(wx.EVT_MENU, self.on_show_history, history_menu_item)
        self.Bind(wx.EVT_MENU, self.on_show_license, license_menu_item)

        # Create the status Bar
        self.SetMenuBar(menu_bar)
        self.statusBar = self.CreateStatusBar(2)
        self.statusBar.SetStatusText("Welcome")


    #Create all the events that are bound to menu items    
    def on_exit(self, e):
        self.Close()

    def on_new_game(self,e):
        wx.MessageBox('Create New Game', 'Menu Selection', wx.OK)

    def on_run_Turn(self,e):
        wx.MessageBox('Run Turn', 'Menu Selection', wx.OK)

    def on_show_map(self,e):
        wx.MessageBox('Show Map', 'Menu Selection', wx.OK)

    def on_show_readme(self,e):
        wx.MessageBox('Show ReadMe', 'Menu Selection', wx.OK)

    def on_show_rules(self,e):
        wx.MessageBox('Show Rules', 'Menu Selection', wx.OK)

    def on_show_license(self,e):
        wx.MessageBox('Show License', 'Menu Selection', wx.OK)

    def on_show_history(self,e):
        wx.MessageBox('Show History', 'Menu Selection', wx.OK)


if __name__ == '__main__':
    app = wx.App()
    frame = REFrame()
    app.MainLoop()
