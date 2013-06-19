get_playable = (container) ->
    urls = container.find('.formats a').map ->
        $(this).attr('href')
    url for url in urls when soundManager.canPlayURL url


show_downloads = (container) ->
    $(container.find '.download').show()


Player = (container) ->

    this.current_name = $(container).find 'track-name'

    controls = $ '<div class="controls"></div>'

    progress = $ '<div class="progress"></div>'

    this.seek = $ '<div></div>'
    this.seek.slider
        range: "min",
        min: -2,
        max: 102,
        value: 0,
        slide: (e, ui) =>
            sound = this.current_track
            new_pos = ui.value * sound.duration / 100
            soundManager.setPosition sound.id, new_pos

    progress.append this.seek

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

    volume = $ '<div class="volume"></div>'

    vol_slide = $ '<div></div>'
    vol_slide.slider
        range: "min",
        min: 0,
        max: 100,
        value: 72,
        slide: (e, ui) =>
            soundManager.setVolume this.current_track.id, ui.value

    volume.append vol_slide

    controls.append progress
    controls.append playnav
    controls.append volume

    container.append controls
    container.append '<div class="clearfix"></div>'

    this.load = (url) =>
        this.current_track = soundManager.createSound
            id: 'mainsound',
            url: url,
            autoLoad: true,
            autoPlay: false,
            whileplaying: ((player)->
                return ->
                    percent = this.position / this.duration * 100
                    player.seek.slider 'value', percent
            ) this

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
            url: '/soundmanager2.swf',  # path to soundmanager2.swf
            onready: ->
                track_url = get_playable player_box
                if not track_url
                    show_downloads player_box
                    return
                player = new Player player_box
                player.load track_url
            ontimeout: ->
                show_downloads player_box

