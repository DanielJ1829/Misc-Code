import matplotlib.pyplot as plt
import numpy as np

#This code plots a square inscribed inside a circle. The figure is intended to be used for an AI education project.

#Figure/axis
fig, ax = plt.subplots(1, 1, figsize=(8, 8))

#Sector Parameters:
radius = 3
theta_degrees = 90  # 90 degree sector (quadrant) - set this as 90 degrees so we can adjust how to frame the question
theta_radians = np.radians(theta_degrees)

#position the 90° corner at the top in the center
center_x = 0
center_y = 2

#Create the sector with vertex at top
#Left edge goes down and left at 45° from vertical by x
#Right edge goes down and right at 45° from vertical by x
left_edge_x = center_x - radius * np.sin(theta_radians/2)
left_edge_y = center_y - radius * np.cos(theta_radians/2)
right_edge_x = center_x + radius * np.sin(theta_radians/2)
right_edge_y = center_y - radius * np.cos(theta_radians/2)

#create arc (bottom of sector) - goes from left endpoint to right endpoint
arc_angles = np.linspace(-3*np.pi/4, -np.pi/4, 100)  # From 225° to 315°
arc_center_x = center_x
arc_center_y = center_y
arc_x = arc_center_x + radius * np.cos(arc_angles)
arc_y = arc_center_y + radius * np.sin(arc_angles)

#plot the outline
ax.plot([center_x, left_edge_x], [center_y, left_edge_y], 'k-', linewidth=2)  # left edge
ax.plot([center_x, right_edge_x], [center_y, right_edge_y], 'k-', linewidth=2)  # right edge
ax.plot(arc_x, arc_y, 'k-', linewidth=2)  # arc

#get the square to sit within the sector correctly
a = np.sqrt(2/5) * radius  # distance between top vertices
square_side = a  # side length of square

#vertices of square:
#on the sector edges:
top_left_x = center_x - a/2
top_left_y = center_y - a/2  # Move down from apex to stay on the left edge
top_right_x = center_x + a/2
top_right_y = center_y - a/2  # Move down from apex to stay on the right edge

#on the arc:
bottom_left_x = top_left_x
bottom_left_y = top_left_y - square_side
bottom_right_x = top_right_x
bottom_right_y = top_right_y - square_side

#turn into lists for the plot
square_x = [top_left_x, top_right_x, bottom_right_x, bottom_left_x, top_left_x]
square_y = [top_left_y, top_right_y, bottom_right_y, bottom_left_y, top_left_y]

#fill the square
ax.fill(square_x, square_y, color='lightgray', alpha=0.7, edgecolor='black', linewidth=1.5)

#labels
#r - on an edge (adjusted afterwards):
label_x = (center_x + right_edge_x) / 2
label_y = (center_y + right_edge_y) / 2
ax.text(label_x+0.2, label_y + 0.3, 'r', fontsize=16, ha='left', va='center', fontweight='bold')

#x - distance between the point where the square vertex and sector edge meet, and the sector vertex
labelx = (center_x + 0.5*right_edge_x)/2
labely = (center_y + 1.5*right_edge_y+1.4)/2
#ax.text(labelx, labely, 'x', fontsize=16, ha='center',va='center', fontweight='light')

#theta - in the arc (adjusted afterwards since automating this is rough):
ax.text(center_x, center_y - 0.27, 'θ', fontsize=16, ha='center', va='bottom', fontweight='light')

#the square - centered
ax.text(center_x, center_y-2, 'A', fontsize=30,ha='center', va='center', fontweight='bold')

#small arc to indicate the angle at the top
small_arc_radius = 0.3
small_angles = np.linspace(-3*np.pi/4, -np.pi/4, 20)
small_arc_x = center_x + small_arc_radius * np.cos(small_angles)
small_arc_y = center_y + small_arc_radius * np.sin(small_angles)
ax.plot(small_arc_x, small_arc_y, 'k-', linewidth=1)

#force equal aspect ratio; clean up the plot
ax.set_aspect('equal')
ax.set_xlim(-3, 3)
ax.set_ylim(-2, 3)

#remove axes/ticks for clarity
ax.set_xticks([])
ax.set_yticks([])
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.spines['bottom'].set_visible(False)
ax.spines['left'].set_visible(False)

plt.tight_layout()
plt.show()