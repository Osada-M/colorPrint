class colorPrint:
    
    """
    cprint = colorPrint().cprint

    cprint(" ~~~ ", color, background, end, **kwargs)
    """

    famous_color = {
            "white"     : "ffffff",
            "lightgray" : "cccccc",
            "gray"      : "aaaaaa",
            "darkgray"  : "666666",
            "black"     : "000000",
            "red"       : "ff4444",
            "orange"    : "ff8844",
            "yellow"    : "ffff33",
            "green"     : "22ff22",
            "lightgreen": "bbffaa",
            "cyan"      : "33eeff",
            "blue"      : "3399ff",
            "purple"    : "ff55dd",
            "pink"      : "ffaaff",
            "brown"     : "bb7733",
        }
    
    
    @staticmethod
    def cprint(string:str="", color:str=None, background:str=None, end:str="\n", **kwargs):
        
        before, after = "", ""
        
        if(color in colorPrint.famous_color.keys()):
            color = colorPrint.famous_color[color]
        if(background in colorPrint.famous_color.keys()):
            background = colorPrint.famous_color[background]
        
        try:
            if color and background:
                red, green, blue = map(lambda x: int(x, 16), [color[2*i:2*i+2] for i in range(3)])
                red_back, green_back, blue_back = map(lambda x: int(x, 16), [background[2*i:2*i+2] for i in range(3)])
                before, after = f"\033[48;2;{red_back};{green_back};{blue_back}m\033[38;2;{red};{green};{blue}m", f"\033[0m\033[0m"
            elif color:
                red, green, blue = map(lambda x: int(x, 16), [color[2*i:2*i+2] for i in range(3)])
                before, after = f"\033[38;2;{red};{green};{blue}m", f"\033[0m"
            elif background:
                red_back, green_back, blue_back = map(lambda x: int(x, 16), [background[2*i:2*i+2] for i in range(3)])
                before, after = f"\033[48;2;{red_back};{green_back};{blue_back}m", f"\033[0m"
            
            print(f"{before}{string}{after}", end=end, **kwargs)
        
        except:
            print(string)
            colorPrint().cprint(f"color input error ! ( color={color}, background={background} )", "ff4444")


