#Requires AutoHotkey v2.0

SetTimer WatchCursor, 100

WatchCursor()
{
    MouseGetPos &xpos, &ypos, &id, &control
    ToolTip
    (
        " X_pos " xpos 
        " Y_pos " ypos
    )
}