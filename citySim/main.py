import pygame
import sys
import random
from scripts.building_data import building_data
from scripts.category_data import category_data
from scripts.citizen_data import citizen_data
from scripts.text_data import good_suggestions, bad_suggestions, mixed_suggestions

# Pygame Initialization
pygame.init()
pygame.mixer.init()
info = pygame.display.Info()
clock = pygame.time.Clock()

# Display Setup
width, height = info.current_w, info.current_h
screen = pygame.display.set_mode((width, height), pygame.FULLSCREEN)
pygame.display.set_caption("City Simulator")

# Grid Setup
cell_width, cell_height = 40, 30
grid_width, grid_height = 60, 50
grid_size = (cell_width, cell_height)

# Camera Setup
camera_x, camera_y = 175, 340
max_camera_x = (grid_width - width // cell_width) * cell_width
max_camera_y = (grid_height - height // cell_height) * cell_height

# Font Setup
info_font = pygame.font.Font(None, 15)
name_font = pygame.font.Font(None, 24)
desc_font = pygame.font.Font(None, 15)
counter_font = pygame.font.Font(None, 18)
small_font = pygame.font.Font(None, 14)

# Image Loading
background_image = pygame.image.load("images/misc/background.png").convert()
grid_image = pygame.image.load("images/misc/grid.png").convert_alpha()

ui_bg_image = pygame.image.load("images/ui/ui_bg.png").convert_alpha()
building_bg_image = pygame.image.load("images/ui/ui_building_bg.png").convert_alpha()
nobuilding_bg_image = pygame.image.load("images/ui/ui_nobuilding_bg.png").convert_alpha()
twitter_bg_image = pygame.image.load("images/ui/ui_twitter_bg.png").convert_alpha()

# Time Setup
update_interval = 10000  # 20 seconds in milliseconds
last_update_time = pygame.time.get_ticks()

# Building and Grid Setup
buildings_list = []
grid = [[0 for _ in range(grid_width)] for _ in range(grid_height)]

building_images = {}
for building_type, rotations in building_data.items():
    for rotation, data in rotations["Rotations"].items():
        image_path = data["ImagePath"]
        building_images[image_path] = pygame.image.load(image_path).convert_alpha()

# Economic Variables
num_population = 0
num_revenue = 0
num_maintenance = 0
num_balance = 10000

# Time Variables
start_date = (2024, 1, 1)
current_date = start_date
days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
time_elapsed = 0
day_duration = 200

# Initial Demand Values
residential_demand = 34
commercial_demand = 33
industrial_demand = 33

# Other Setup
button_images = {category: pygame.image.load(data["ImagePath"]).convert_alpha() for category, data in category_data.items()}
button_size = (60, 60)
selected_building_preview = {"type": "road_3way", "rotation": "north", "x": 0, "y": 0}
active_category = None
prev_mouse_state = 0
show_grid = False
time_paused = False


# Functions

def screen_to_grid(screen_x, screen_y):
    return (screen_x + camera_x) // cell_width, (screen_y + camera_y) // cell_height

def is_mouse_over_ui(mouse_y):
    return mouse_y > height - 125 - 100 if active_category else mouse_y > height - 125

def is_space_free(x, y, width, height, grid):
    for i in range(width):
        for j in range(height):
            if grid[y + j][x + i] == 1:
                return False
    return True

def is_valid_position(building_type, grid_x, grid_y, building_rotation, buildings_list):
    building_width, building_height = building_data[building_type]["Rotations"][building_rotation]["Width"], building_data[building_type]["Rotations"][building_rotation]["Height"]
    if not (0 <= grid_x < grid_width and 0 <= grid_y < grid_height):
        return False
    return all(
        not (building["x"] < grid_x + building_width and building["x"] + building_data[building["type"]]["Rotations"][building["rotation"]]["Width"] > grid_x and
            building["y"] < grid_y + building_height and building["y"] + building_data[building["type"]]["Rotations"][building["rotation"]]["Height"] > grid_y )
        for building in buildings_list
    )

def is_mouse_in_building(building, mouse_x, mouse_y):
    building_type, building_rotation = building["type"], building["rotation"]
    building_data_rotated = building_data[building_type]["Rotations"][building_rotation]
    building_rect = pygame.Rect(building["x"] * cell_width - camera_x, building["y"] * cell_height - camera_y,
                               building_data_rotated["Width"] * cell_width, building_data_rotated["Height"] * cell_height)
    return building_rect.collidepoint(mouse_x, mouse_y)

def tint_building_image(building_image, tint_color):
    tinted_image = building_image.copy()
    tinted_image.fill(tint_color, special_flags=pygame.BLEND_RGBA_MULT)
    tinted_image.set_alpha(128)
    return tinted_image

def render_building_preview(building_type, building_rotation, mouse_x, mouse_y):
    grid_x, grid_y = screen_to_grid(mouse_x, mouse_y)
    tint_color = (50, 200, 50) if is_valid_position(building_type, grid_x, grid_y, building_rotation, buildings_list) else (200, 50, 50)
    render_x, render_y = grid_x * cell_width - camera_x - cell_width, grid_y * cell_height - camera_y - cell_height
    image_path = building_data[building_type]["Rotations"][building_rotation]['ImagePath']
    screen.blit(tint_building_image(building_images[image_path], tint_color), (render_x, render_y))

def rotate_building(selected_building_preview):
    current_rotation, rotations = selected_building_preview["rotation"], ["north", "east", "south", "west"]
    next_rotation_index = (rotations.index(current_rotation) + 1) % len(rotations)
    selected_building_preview["rotation"] = rotations[next_rotation_index]

def render_building(building, camera_x, camera_y):
    building_type, building_rotation, building_x, building_y = building["type"], building["rotation"], building["x"], building["y"]
    render_x, render_y = building_x * cell_width - camera_x - cell_width, building_y * cell_height - camera_y - cell_height
    image_path = building_data[building_type]["Rotations"][building_rotation]['ImagePath']
    screen.blit(building_images[image_path], (render_x, render_y))

def draw_ui_button(category, rect):
    button_image = button_images[category]
    screen.blit(pygame.transform.scale(button_image, button_size), rect.topleft)

def draw_ui():
    global active_category, prev_mouse_state, current_date

    ui_surface = pygame.Surface((width, 125), pygame.SRCALPHA)
    ui_surface.blit(pygame.transform.scale(ui_bg_image, (width, 125)), (0, 0))
    screen.blit(ui_surface, (0, height - 125))

    total_buttons_width = len(category_data) * (button_size[0] + 25) - 25
    starting_x = (width - total_buttons_width) // 2
    starting_y = height - 115

    mouse_state = pygame.mouse.get_pressed()[0]

    for category, data in category_data.items():
        button_rect = pygame.Rect(starting_x, starting_y, *button_size)
        mouse_x, mouse_y = pygame.mouse.get_pos()
        if button_rect.collidepoint(mouse_x, mouse_y) and mouse_state and not prev_mouse_state:
            active_category = None if active_category == category else category
        draw_ui_button(category, button_rect)
        starting_x += button_size[0] + 20

    prev_mouse_state = mouse_state

    city_rating = calculate_city_rating(buildings_list)

    rating_text = f"{city_rating}/100"
    date_text = update_time()
    balance_text = f"{num_balance}"
    revenue_text = f"${num_revenue}p/w"
    maintenance_text = f"${num_maintenance}p/w"
    population_text = f"{num_population}"

    text_info = [
        (name_font, balance_text, (255, 255, 255), (577, height - 35), 'topleft'),
        (small_font, revenue_text, (130, 190, 130), (722, height - 39), 'topright'),
        (small_font, maintenance_text, (190, 130, 130), (722, height - 26), 'topright'),
        (name_font, population_text, (255, 255, 255), (777, height - 35), 'topleft'),
        (name_font, date_text, time_text_color, (977, height - 35), 'topleft'),
        (name_font, rating_text, (255, 255, 255), (1177, height - 35), 'topleft')
    ]


    for font, text, color, position, anchor in text_info:
        text_render = font.render(text, True, color)
        if anchor == 'topleft':
            text_rect = text_render.get_rect(topleft=position)
        elif anchor == 'topright':
            text_rect = text_render.get_rect(topright=position)
        screen.blit(text_render, text_rect.topleft)

    pygame.draw.rect(screen, (0, 255, 0), pygame.Rect(150, height - 80, residential_demand, 10))  # Green for Res
    pygame.draw.rect(screen, (0, 0, 255), pygame.Rect(150, height - 60, commercial_demand, 10))  # Blue for Com
    pygame.draw.rect(screen, (255, 165, 0), pygame.Rect(150, height - 40, industrial_demand, 10))  # Orange for Ind

    draw_category_frames()

def draw_category_frames():
    prev_mouse_state = False
    
    if active_category is not None:
        frame_rect = pygame.Rect(0, height - 100 - 125, width, 100)
        frame_background = pygame.transform.scale(building_bg_image, frame_rect.size)
        screen.blit(frame_background, frame_rect.topleft)

        category_buildings = [building for building in building_data.values() if building['Category'] == active_category]
        building_width = (width - 2 * 0 - (len(category_buildings) - 1) * 0) // len(category_buildings)

        for idx, building in enumerate(category_buildings):
            x_position = 0 + idx * (building_width + 0)
            button_background_rect = pygame.Rect(x_position, height - 125 - 80, building_width, 80)

            mouse_x, mouse_y = pygame.mouse.get_pos()

            if button_background_rect.collidepoint(mouse_x, mouse_y):
                if pygame.mouse.get_pressed()[0] and not prev_mouse_state:
                    selected_building_preview["type"] = building["Type"]

            name_render, desc_render = name_font.render(building['Name'], True, (255, 255, 255)), desc_font.render(building['Description'], True, (255, 255, 255))
            name_text_rect, desc_text_rect = name_render.get_rect(midtop=(x_position + building_width / 2, height - 200)), desc_render.get_rect(midtop=(x_position + building_width / 2, height - 180))
            screen.blit(name_render, name_text_rect)
            screen.blit(desc_render, desc_text_rect)

            necessary_info = building.get('Information', [])
            info_text_lines = [
                f"{info}: ${building[info]}p/w" if info in ['Revenue', 'Maintenance'] else f"{info}: ${building[info]}" if info == 'Cost' else f"{info}: +{building[info]}" for info in necessary_info
            ]
            info_text = '\n'.join(info_text_lines)
            info_render = info_font.render(info_text, True, (255, 255, 255))
            info_text_rect = info_render.get_rect(midtop=(x_position + building_width / 2, height - 125 - 40))
            screen.blit(info_render, info_text_rect)

        prev_mouse_state = pygame.mouse.get_pressed()[0]
    else:
        frame_rect = pygame.Rect(0, height - 125 - 100, width, 0)
        screen.blit(nobuilding_bg_image, frame_rect.topleft)

def render_tweet_box(text, name, handle):
    box_width, box_height = 350, 70
    box_padding = 13

    # Create a surface for the tweet box
    tweet_box_surface = pygame.Surface((box_width, box_height), pygame.SRCALPHA)
    tweet_box_surface.blit(twitter_bg_image, (0, 0))

    name_render = name_font.render(name, True, (230, 230, 230))  # Fix: Use text_color for name text
    name_rect = name_render.get_rect(topleft=(box_padding, box_padding))
    tweet_box_surface.blit(name_render, name_rect.topleft)

    handle_render = desc_font.render(f'{handle}', True, (150, 150, 150))  # Add handle text
    handle_rect = handle_render.get_rect(topleft=(box_padding, name_rect.bottom + 1))
    tweet_box_surface.blit(handle_render, handle_rect.topleft)

    text_render = desc_font.render(text, True, (255, 255, 255))
    text_rect = text_render.get_rect(topleft=(box_padding, handle_rect.bottom + 7))
    tweet_box_surface.blit(text_render, text_rect.topleft)

    # Render the tweet box on the main screen
    screen.blit(tweet_box_surface, (width - box_width - box_padding, box_padding))

def calculate_city_rating(buildings_list):
    total_score = 0
    building_scores = {}

    for building in buildings_list:
        building_type = building["type"]
        building_score = building_data.get(building_type, {}).get("Score", 0)

        building_scores[building_type] = building_scores.get(building_type, 0) + 1
        modified_score = building_score / (3 ** (building_scores[building_type] - 1))
        total_score += modified_score

    city_rating = min(int((total_score / 100) * 100), 100)

    return city_rating

def update_time():
    global current_date, time_elapsed, num_balance, time_paused, time_text_color

    if not time_paused:
        time_elapsed += clock.get_rawtime()
        if time_elapsed >= day_duration:
            time_elapsed -= day_duration
            year, month, day = current_date
            day += 1
            if day > days_in_month[month - 1]:
                day = 1
                month += 1
                if month > 12:
                    month = 1
                    year += 1
            current_date = (year, month, day)

            # Calculate and update balance at the end of each week
            if day % 7 == 0:  # Assuming a week is 7 days
                weekly_balance_change = num_revenue - num_maintenance
                num_balance += weekly_balance_change

    time_text_color = (255, 0, 0) if time_paused else (255, 255, 255)
    return f"{current_date[2]} / {current_date[1]} / {current_date[0]}"

running = True

def update_rci_demand(buildings_list, residential_demand, commercial_demand, industrial_demand):
    for building in buildings_list:
        building_info = building_data.get(building["type"], None)

        if building_info:
            building_category = building_info.get("Category", None)

            if building_category == "Residential":
                residential_demand -= 2
                commercial_demand += 1
                industrial_demand += 1
            elif building_category == "Commercial":
                residential_demand += 1
                commercial_demand -= 2
                industrial_demand += 1
            elif building_category == "Industrial":
                residential_demand += 1
                commercial_demand += 1
                industrial_demand -= 2

    return residential_demand, commercial_demand, industrial_demand




while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_g:
                show_grid = not show_grid
            elif event.key == pygame.K_r:
                rotate_building(selected_building_preview)
            elif event.key == pygame.K_SPACE:
                time_paused = not time_paused

        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            if not is_mouse_over_ui(mouse_y):
                if event.button == 1:
                    grid_x, grid_y = screen_to_grid(mouse_x, mouse_y)
                    building_type = selected_building_preview["type"]
                    building_rotation = selected_building_preview["rotation"]
                    building_width = building_data[building_type]["Rotations"][building_rotation]['Width']
                    building_height = building_data[building_type]["Rotations"][building_rotation]['Height']

                    if is_space_free(grid_x, grid_y, building_width, building_height, grid):
                        action = 1  # 1 for placement
                        for i in range(building_width):
                            for j in range(building_height):
                                grid[grid_y + j][grid_x + i] = action
                        buildings_list.append({"type": building_type, "rotation": building_rotation, "x": grid_x, "y": grid_y})
                        num_balance -= building_data[building_type]['Cost']
                        num_maintenance += building_data[building_type]['Maintenance']
                        num_revenue += building_data[building_type]['Revenue']
                        num_population += building_data[building_type]['Population']
                        residential_demand, commercial_demand, industrial_demand = update_rci_demand(buildings_list, residential_demand, commercial_demand, industrial_demand)

                    
                elif event.button == 3:
                    action = 0  # 0 for deletion
                    for building in buildings_list:
                        if is_mouse_in_building(building, mouse_x, mouse_y):
                            building_width = building_data[building["type"]]["Rotations"][building["rotation"]]['Width']
                            building_height = building_data[building["type"]]["Rotations"][building["rotation"]]['Height']
                            for i in range(building_width):
                                for j in range(building_height):
                                    grid[building["y"] + j][building["x"] + i] = action
                            buildings_list.remove(building)
                            num_balance += int(building_data[building_type]['Cost'] * 0.75)
                            num_maintenance -= building_data[building_type]['Maintenance']
                            num_revenue -= building_data[building_type]['Revenue']
                            num_population -= building_data[building_type]['Population']
                            residential_demand, commercial_demand, industrial_demand = update_rci_demand(buildings_list, residential_demand, commercial_demand, industrial_demand)

    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        camera_y = max(0, camera_y - 5)
    if keys[pygame.K_s]:
        camera_y = min(max_camera_y, camera_y + 5)
    if keys[pygame.K_a]:
        camera_x = max(0, camera_x - 5)
    if keys[pygame.K_d]:
        camera_x = min(max_camera_x, camera_x + 5)

    screen.blit(background_image, (-camera_x, -camera_y))

    for building in sorted(buildings_list, key=lambda b: (b["y"], b["x"]), reverse=False):
        render_building(building, camera_x, camera_y)

    if show_grid:
        screen.blit(grid_image, (-camera_x, -camera_y))

    if selected_building_preview:
        selected_building_type = selected_building_preview["type"]
        selected_building_rotation = selected_building_preview["rotation"]
        render_building_preview(selected_building_type, selected_building_rotation, *pygame.mouse.get_pos())  

    current_time = pygame.time.get_ticks()

    draw_ui()

    fps = int(clock.get_fps())
    fps_text = name_font.render(f"FPS: {fps}", True, (0, 0, 0))
    screen.blit(fps_text, (10, 10))

    city_rating = calculate_city_rating(buildings_list)

    if current_time - last_update_time >= update_interval:
        random_name, twitter_handle = random.choice(list(citizen_data.items()))
        if city_rating >= 80:
            suggestion = random.choice(good_suggestions)
        elif 60 <= city_rating < 80:
            suggestion = random.choice(mixed_suggestions)
        else:
            suggestion = random.choice(bad_suggestions)
        last_update_time = current_time

    if 'suggestion' in locals():
        render_tweet_box(suggestion, random_name, twitter_handle)

    clock.tick(60)
    
    pygame.display.update()
