get_playable = (container) ->
    urls = container.find('.formats a').map ->
        $(this).attr('href')
    url for url in urls when soundManager.canPlayURL url


show_downloads = (container) ->
    $(container.find '.download').show()


Player = (container) ->

    controls = $ '<div class="controls"></div>'

    progress = $ '<div class="progress">progress</div>'

    playnav = $ '<div class="playnav"></div>'

    this.add_nav_button = (action, name, symbol) ->
        button = $ '<a href="#' + action + '" title="' + name + '">' + symbol + '</a>'
        playnav.append button
        button.click =>
            this.nav action
            return false

    this.add_nav_button "pause", "Pause", "◫"
    this.add_nav_button "stop", "Stop", "■"
    this.add_nav_button "play", "Play", "▶"
    this.add_nav_button "prev", "Previous", "↞"
    this.add_nav_button "next", "Next", "↠"

    playnav.append '<div class="clearfix"></div>'

    volume = $ '<div class="volume">volume</div>'

    controls.append progress
    controls.append playnav
    controls.append volume

    container.append controls

    this.load = (url) ->
        this.current_track = soundManager.createSound
            id: 'mainsound',
            url: url,
            autoLoad: true,
            autoPlay: false,
            onload: ->
                console.log 'loaded the track! '

    this.nav = (action) ->
        sound = this.current_track
        switch action
            when 'pause' then sound.pause()
            when 'stop' then sound.stop()
            when 'play' then sound.play()

    return this



$ ->
    player_box = $ "#music-player"

    if player_box.length  # exists?

        soundManager.setup
            url: SM2SWFPath,  # path to soundmanager2.swf
            onready: ->
                console.log 'rrrrrerady'
                track_url = get_playable player_box
                if not track_url
                    show_downloads player_box
                    return
                player = new Player player_box
                player.load track_url
            ontimeout: ->
                show_downloads player_box

