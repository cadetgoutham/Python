"""
Interactive Fidget Spinner Simulation

Description:
    A self-contained Pygame application simulating a rotating fidget spinner.
    Features physics implementation including interactive motor acceleration, 
    friction-based deceleration, color customization, and runtime metrics telemetry.

Controls:
    - RIGHT ARROW : Spin clockwise (Accelerate)
    - LEFT ARROW  : Spin counter-clockwise (Accelerate)
    - SPACEBAR    : Toggle color themes
    - Q / CLOSE   : Exit application

Requirements:
    $ pip install pygame-ce

How to Run:
    $ python fidget_spinner.py
"""

import sys
import math
import pygame

# Initialize structural styling variables
WINDOW_WIDTH = 500
WINDOW_HEIGHT = 500
FPS = 90

# Define Application Color Palette
BACKGROUND_COLOR = (51, 51, 51)
WHITE = (240, 240, 240)
DARK_GRAY = (23, 32, 42)

# Spinner theme matrices [Primary Color, Accent Highlight Color]
COLOR_THEMES = [
    [(176, 58, 46), (120, 40, 31)],     # Red / Dark Red
    [(40, 116, 166), (26, 82, 118)],    # Blue / Dark Blue
    [(183, 149, 11), (125, 102, 8)],    # Yellow / Dark Yellow
    [(29, 131, 72), (20, 90, 50)],      # Green / Dark Green
    [(230, 126, 34), (126, 81, 9)]      # Orange / Dark Orange
]


def terminate_session():
    """Cleanly exits Pygame and system operations."""
    pygame.quit()
    sys.exit()


def draw_fidget_spinner(surface, angle, colors):
    """
    Computes trigonometric offsets and draws the multi-jointed spinner body.
    """
    primary_color, accent_color = colors
    
    # Structural geometry constraints
    outer_diameter = 80
    inner_diameter = 50
    arm_length = 200
    line_thickness = 60
    
    # Pre-calculated mathematical constants
    sqrt_three = math.sqrt(3)
    rotation_radius = arm_length / sqrt_three
    
    # Calculate screen center point references
    center_x = WINDOW_WIDTH / 2 - outer_diameter / 2
    center_y = WINDOW_HEIGHT / 2
    inner_offset = outer_diameter / 2 - inner_diameter / 2

    # Initialize geometry structures
    center_outer_rect = [center_x, center_y, outer_diameter, outer_diameter]
    center_inner_rect = [center_x + inner_offset, center_y + inner_offset, inner_diameter, inner_diameter]
    
    # Allocate bounding arrays for the three rotating arms
    top_outer = [0, 0, outer_diameter, outer_diameter]
    top_inner = [0, 0, inner_diameter, inner_diameter]
    left_outer = [0, 0, outer_diameter, outer_diameter]
    left_inner = [0, 0, inner_diameter, inner_diameter]
    right_outer = [0, 0, outer_diameter, outer_diameter]
    right_inner = [0, 0, inner_diameter, inner_diameter]

    # Compute explicit spatial coordinates using polar-to-rectangular conversion
    # x = center_x + radius * cos(angle)
    # y = center_y + radius * sin(angle)
    
    # Top Node Position Calculation
    top_outer[0] = center_x + rotation_radius * math.cos(math.radians(angle))
    top_outer[1] = center_y + rotation_radius * math.sin(math.radians(angle))
    top_inner[0] = center_x + inner_offset + rotation_radius * math.cos(math.radians(angle))
    top_inner[1] = center_y + inner_offset + rotation_radius * math.sin(math.radians(angle))
    
    # Left Node Position Calculation (Offset -120 degrees)
    left_outer[0] = center_x + rotation_radius * math.cos(math.radians(angle - 120))
    left_outer[1] = center_y + rotation_radius * math.sin(math.radians(angle - 120))
    left_inner[0] = center_x + inner_offset + rotation_radius * math.cos(math.radians(angle - 120))
    left_inner[1] = center_y + inner_offset + rotation_radius * math.sin(math.radians(angle - 120))
    
    # Right Node Position Calculation (Offset +120 degrees)
    right_outer[0] = center_x + rotation_radius * math.cos(math.radians(angle + 120))
    right_outer[1] = center_y + rotation_radius * math.sin(math.radians(angle + 120))
    right_inner[0] = center_x + inner_offset + rotation_radius * math.cos(math.radians(angle + 120))
    right_inner[1] = center_y + inner_offset + rotation_radius * math.sin(math.radians(angle + 120))
    
    # Step 1: Render structural connecting bone framework
    center_joint_pos = (center_x + outer_diameter / 2, center_y + outer_diameter / 2)
    pygame.draw.line(surface, accent_color, (top_outer[0] + outer_diameter / 2, top_outer[1] + outer_diameter / 2), center_joint_pos, line_thickness)
    pygame.draw.line(surface, accent_color, (left_outer[0] + outer_diameter / 2, left_outer[1] + outer_diameter / 2), center_joint_pos, line_thickness)
    pygame.draw.line(surface, accent_color, (right_outer[0] + outer_diameter / 2, right_outer[1] + outer_diameter / 2), center_joint_pos, line_thickness)
    
    # Step 2: Render inner/outer component nodes
    pygame.draw.ellipse(surface, primary_color, tuple(center_outer_rect))
    pygame.draw.ellipse(surface, accent_color, tuple(center_inner_rect))
    
    pygame.draw.ellipse(surface, primary_color, tuple(top_outer))
    pygame.draw.ellipse(surface, DARK_GRAY, tuple(top_inner), 10)
    
    pygame.draw.ellipse(surface, primary_color, tuple(left_outer))
    pygame.draw.ellipse(surface, DARK_GRAY, tuple(left_inner), 10)
    
    pygame.draw.ellipse(surface, primary_color, tuple(right_outer))
    pygame.draw.ellipse(surface, DARK_GRAY, tuple(right_inner), 10)


def draw_telemetry_ui(surface, friction, angular_velocity):
    """Renders debug performance metrics cleanly in the top-left quadrant."""
    font = pygame.font.SysFont("Times New Roman", 18)
    friction_surface = font.render(f"Friction: {friction:.2f}", True, WHITE)
    velocity_surface = font.render(f"Angular Velocity: {angular_velocity:.2f}", True, WHITE)
    
    surface.blit(velocity_surface, (15, 15))
    surface.blit(friction_surface, (15, 45))


def run_simulation():
    """Initializes hardware wrappers and drives core engine cycle steps."""
    pygame.init()
    display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    pygame.display.set_caption("Fidget Spinner Simulation")
    execution_clock = pygame.time.Clock()

    current_angle = 0.0
    angular_velocity = 0.0
    friction_coefficient = 0.03
    
    is_accelerating_clockwise = False
    is_accelerating_counter_clockwise = False
    spin_direction = 1
    current_theme_index = 0
    is_running = True
    
    while is_running:
        # Check event bus for operational state updates
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate_session()
                
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    terminate_session()
                elif event.key == pygame.K_RIGHT:
                    is_accelerating_clockwise = True
                    spin_direction = 1
                elif event.key == pygame.K_LEFT:
                    is_accelerating_counter_clockwise = True
                    spin_direction = -1
                elif event.key == pygame.K_SPACE:
                    current_theme_index = (current_theme_index + 1) % len(COLOR_THEMES)
                    
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_RIGHT:
                    is_accelerating_clockwise = False
                elif event.key == pygame.K_LEFT:
                    is_accelerating_counter_clockwise = False

        # Apply simulation kinematics physics modifications
        if spin_direction == 1:
            if is_accelerating_clockwise:
                angular_velocity += 1.0
            else:
                angular_velocity -= friction_coefficient
                if angular_velocity < 0:
                    angular_velocity = 0.0
        else:
            if is_accelerating_counter_clockwise:
                angular_velocity -= 0.3
            else:
                angular_velocity += friction_coefficient
                if angular_velocity > 0:
                    angular_velocity = 0.0
                    
        # Redraw frame composition layer updates
        display_surface.fill(BACKGROUND_COLOR)
        current_angle += angular_velocity

        draw_fidget_spinner(display_surface, current_angle, COLOR_THEMES[current_theme_index])
        draw_telemetry_ui(display_surface, friction_coefficient, angular_velocity)
        
        pygame.display.update()
        execution_clock.tick(FPS)


if __name__ == "__main__":
    run_simulation()