from pycaw.pycaw import AudioUtilities, ISimpleAudioVolume

def set_game_mute(target_exe_name, mute_state):
    """
    mute_state = 1 -> Sessize alir
    mute_state = 0 -> Sesi tekrar açar
    """
    try:
        sessions = AudioUtilities.GetAllSessions()
        for session in sessions:
            if session.Process and session.Process.name() == target_exe_name:
                volume = session._ctl.QueryInterface(ISimpleAudioVolume)
                volume.SetMute(mute_state, None)
                status = "sessize alındı" if mute_state == 1 else "sesi açıldı"
                print(f"{target_exe_name} {status}.")
                return True
        print(f"{target_exe_name} aktif ses oturumu bulunamadı.")
    except Exception as e:
        print(f"Ses durumu değiştirilirken hata oluştu: {e}")
    return False