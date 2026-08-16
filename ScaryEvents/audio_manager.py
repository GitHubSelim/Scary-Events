import pulsectl

def set_game_mute(target_exe_name, mute_state):
    """
    mute_state = 1 -> Sessize alir
    mute_state = 0 -> Sesi tekrar açar
    """

    with pulsectl.Pulse("ses-ayarlayici") as pulse:
        # application.name == target_exe_name olan tüm sink input'ları ayarla
        for sink in pulse.sink_input_list():
            if sink.proplist.get("application.name") != target_exe_name:
                continue

            pulse.mute(sink, mute_state)
