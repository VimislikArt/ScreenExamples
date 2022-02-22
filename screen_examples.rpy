screen jump_to_the_question:
    frame:
        xpadding 50
        ypadding 30
        xalign 0.9
        yalign 0.1
        textbutton "THE QUESTION" action [ToggleScreen("jump_to_the_question"), Jump("the_question")]

screen textmiddle:
    fixed:
        ypos -200
        xpos 500
        image "eileen concerned.png" zoom 2.0 blur 10.0
    frame:
        xpadding 40
        ypadding 20
        xalign 0.5
        yalign 0.5
        text "this text is in the middle"

screen text_verticalgrid:
    vbox:
        xalign 0.5
        yalign 0.5
        spacing 20
        frame:
            xpadding 40
            ypadding 20
            xalign 0.5
            yalign 0.5
            text "this text is on the top"
        frame:
            xpadding 40
            ypadding 20
            xalign 0.5
            yalign 0.5
            text "this text is on the bottom"

screen text_horizontalgrid:
    hbox:
        xalign 0.5
        yalign 0.5
        spacing 20
        frame:
            xpadding 40
            ypadding 20
            xalign 0.5
            yalign 0.5
            text "this text is on the left"
        frame:
            xpadding 40
            ypadding 20
            xalign 0.5
            yalign 0.5
            text "this text is on the right"

screen text_2x2grid:
    grid 2 2:
        xalign 0.5
        yalign 0.5
        spacing 20
        frame:
            xpadding 40
            ypadding 20
            xalign 0.5
            yalign 0.5
            text "TextBlock 1"
        frame:
            xpadding 40
            ypadding 20
            xalign 0.5
            yalign 0.5
            text "TextBlock2"
        frame:
            xpadding 40
            ypadding 20
            xalign 0.5
            yalign 0.5
            text "TextBlock3"
        frame:
            xpadding 40
            ypadding 20
            xalign 0.5
            yalign 0.5
            text "TextBlock4"

screen button_overlay():
    mousearea:
        area (0, 0, 1.0, 100)
        hovered Show("buttons", transition=dissolve)
        unhovered Hide("buttons", transition=dissolve)
screen preferences():

    tag menu
    use navigation

    imagemap:
        auto "gui_set/gui_prefs_%s.png"

        hotspot (740, 232, 75, 73) action Preference("display", "fullscreen") alt _("Display Fullscreen")
        hotspot (832, 232, 75, 73) action Preference("display", "window") alt _("Display Window")
        hotspot (1074, 232, 75, 73) action Preference("transitions", "all") alt _("Transitions All")
        hotspot (1166, 232, 75, 73) action  Preference("transitions", "none") alt _("Transitions None")

        hotbar (736, 415, 161, 20) value Preference("music volume") alt _("Music Volume")
        hotbar (1070, 415, 161, 20) value Preference("sound volume") alt _("Sound Volume")
        hotbar (667, 535, 161, 20) value Preference("voice volume") alt _("Voice Volume")
        hotbar (1001, 535, 161, 20) value Preference("text speed") alt _("Text Speed")


screen input_screen:
    frame:
        xalign 0.5
        yalign 0.5
        ypadding 50
        xpadding 100
        has vbox

        text "Input some text!"
        input default "Right in here!" value VariableInputValue("the_text")

        frame:
            top_margin 50
            xpadding 20
            ypadding 10
            textbutton "I'm done typing text" action Return(value="the_text")


screen textadd:
    hbox:
        xalign 0.5
        yalign 0.5
        spacing 20
        vbox:

            frame:
                xpadding 40
                ypadding 20
                xalign 0.5
                yalign 0.5
                if initialvalue <=9:
                    textbutton "{size=+30}+1{/size}" action SetVariable("initialvalue", initialvalue + 1)
                else:
                    text "{size=+30}X{/size}"
            frame:
                xpadding 40
                ypadding 20
                xalign 0.5
                yalign 0.5
                if initialvalue >= 1:
                    textbutton "{size=+30}-1{/size}" action SetVariable("initialvalue", initialvalue - 1)
                else:
                    textbutton "{size=+30}X{/size}" action NullAction()

        vbox:
            xalign 0.5
            yalign 0.5
            spacing 20
            frame:
                xpadding 40
                ypadding 20
                xalign 0.5
                yalign 0.5
                text "The Number is [initialvalue]."
