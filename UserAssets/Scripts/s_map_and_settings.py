from UserAssets.Scripts.basics import *# Engine Area__id__ = 'settings'game_on = False# Globalzombies_left = 10music = Music('mMain')# TEXTtext_transform = Transform2D()on_screen_text = PlainText('Alive: ', line_width=2)# In Game Mapmap_transform = Transform2D()map_border = SpriteRenderer('map_border.png', smooth=False)map_floor = SpriteRenderer('floor_2.jpg', smooth=False)def Start():    global last_capsule_spawn    music.play(-1)    last_capsule_spawn = 0    # camera settings    Camera.screen_mode()    Camera.clearColor = Vector3.ones(0.2)    # text settings    text_transform.scale = Vector3.ones(6)    text_transform.position = Vector3(-5, 5, -5)    map_transform.scale = Vector3.ones(50)def Events(event_name, *args):    global game_on    # start rendering only when start button is pressed    if event_name == 'start_the_game':        save_data_base()        game_on = Truedef Render():    global game_on    if game_on:        # map        glPushMatrix()        map_transform.applyTransformation()        map_floor.render(mul=25, brightness=0.3)        map_border.render()        glPopMatrix()        # Text        glPushMatrix()        text_transform.applyTransformation()        on_screen_text.render(color=Vector3.ones())        glPopMatrix()def Update():    global last_capsule_spawn    if game_on and Time.fixedTime > last_capsule_spawn + 15:        last_capsule_spawn = Time.fixedTime        target_pos = get_script('player').transform.position + random_point_on_unit_circle() * 25        instantiate_script('hp_capsule').transform.position = target_pos    if zombies_left <= 0:        instantiate_script('victory_screen')        castEvent('pause_the_game', None)def LateUpdate():    Camera.position = Vector3.clap_magnitude(Camera.position, 0, 50)    text_transform.position = Camera.screenToWorld(Vector3(-1, 1, 0)) + Vector3(.2, -1, 0)    on_screen_text.text = 'Alive:' + str(int(zombies_left)) + '\t HP:' + str(int(get_script('player').current_hp))