import json
import uuid
from pathlib import Path


# You can use any file from Colorizah
# https://github.com/runxel/colorizah
COL_INPUT = "ral-classic.json"

REFID_SURF = 1296127026


def hex_to_unsigned_short(hex_value):
	"""Convert a 2-digit hex value (00-FF) to unsigned short (0-65535)"""
	decimal = int(hex_value, 16)
	return int((decimal / 255) * 65535)


def parse_hex_color(hex_color):
	"""Parse a 6-digit hex color into RGB unsigned short values"""
	# Remove '#' if present
	hex_color = hex_color.lstrip("#")

	# Extract RGB components
	r = hex_to_unsigned_short(hex_color[0:2])
	g = hex_to_unsigned_short(hex_color[2:4])
	b = hex_to_unsigned_short(hex_color[4:6])

	return r, g, b


def create_material_xml(name, index, r, g, b):
	"""Create a Material xml node."""
	guid = str(uuid.uuid4()).upper()

	return f"""			<Material>
				<OdbObj>
					<OdbRef>
						<guid>{guid}</guid>
					</OdbRef>
				</OdbObj>
				<Name>{name}</Name>
				<Index>{index}</Index>
				<Flags/>
				<ModiTime>0</ModiTime>
				<RegMemoTable MemoNumber="0" Mv="1" Sv="0"/>
				<ImageAttributes>
					<Type>20</Type>
					<SurfaceColor>
						<Red>{r}</Red>
						<Green>{g}</Green>
						<Blue>{b}</Blue>
					</SurfaceColor>
					<AmbientReflection>90</AmbientReflection>
					<DiffuseReflection>90</DiffuseReflection>
					<SpecularReflection>10</SpecularReflection>
					<Transparency>0</Transparency>
					<Shine>90</Shine>
					<TransparencyAttenuation>0</TransparencyAttenuation>
					<SpecularColor>
						<Red>65535</Red>
						<Green>65535</Green>
						<Blue>65535</Blue>
					</SpecularColor>
					<EmissionColor>
						<Red>0</Red>
						<Green>0</Green>
						<Blue>0</Blue>
					</EmissionColor>
					<EmissionAttenuation>0</EmissionAttenuation>
				</ImageAttributes>
				<FillIndex>65</FillIndex>
				<Name/>
				<TextStatus>0</TextStatus>
				<FillColor>-1</FillColor>
				<XSize>1</XSize>
				<YSize>1</YSize>
				<RotationAngle>0</RotationAngle>
			</Material>"""


def convert_json_to_xml(json_file_path, output_file_path):
	"""Convert Colorizah JSON to Archicad XML format"""

	# Read JSON file
	with open(json_file_path, "r", encoding="utf-8") as f:
		data = json.load(f)

	colors = data["colorsystem"]["colors"]
	materials = []

	# Process each color
	for index, color in enumerate(colors, start=1):
		name = f"RAL {color['id']} – {color['vanityname']}"
		r, g, b = parse_hex_color(color["hex"])
		material_xml = create_material_xml(name, index, r, g, b)
		materials.append(material_xml)

	# Combine all materials
	materials_xml = "\n".join(materials)

	# Create final XML
	num_colors = len(colors)
	final_xml = f"""<?xml version="1.0" encoding="UTF-8"?>
<AttributeFile>
	<RegisteredAttributes>
		<NumberOfRegisteredAttributes>1</NumberOfRegisteredAttributes>
		<Attributes>
			<RefID>{REFID_SURF}</RefID>
{materials_xml}
		</Attributes>
	</RegisteredAttributes>
</AttributeFile>"""

	# Write to output file
	with open(output_file_path, "w", encoding="utf-8") as f:
		f.write(final_xml)

	print(f"Successfully converted {num_colors} colors to {output_file_path}")


if __name__ == "__main__":
	# Set paths
	script_dir = Path(__file__).parent
	json_file = script_dir / COL_INPUT
	_out = Path(COL_INPUT).stem + ".xml"
	output_file = script_dir.parent / "Surfaces" / _out

	# Convert
	convert_json_to_xml(json_file, output_file)
