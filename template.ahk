#Requires AutoHotkey v2.0

; MsgBox("Arrange: Me`nOrigin: THE_AUTHOR", "Credits")

TEMPO := 69
MINUTE := 60 * 1000

note16(key) {
    Send key
    Sleep MINUTE / TEMPO / 4
}

stroke(keys*) {
    for key in keys
        note16(key)
}

^e::ExitApp

^0::{
}
