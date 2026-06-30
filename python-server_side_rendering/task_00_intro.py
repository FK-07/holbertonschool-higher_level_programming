#!/usr/bin/python3
"""
Simple Templating Program to generate personalized invitation files.
"""
import os


def generate_invitations(template, attendees):
    """
    Generates invitation files from a template and a list of attendee dicts.
    """
    # Verify input types
    if not isinstance(template, str):
        print("Invalid input type: template must be a string.")
        return

    if not isinstance(attendees, list) or not all(
        isinstance(a, dict) for a in attendees
    ):
        print("Invalid input type: attendees must be a list of dictionaries.")
        return

    # Handle empty inputs
    if not template.strip():
        print("Template is empty, no output files generated.")
        return

    if not attendees:
        print("No data provided, no output files generated.")
        return

    # Process each attendee
    keys = ["name", "event_title", "event_date", "event_location"]

    for idx, attendee in enumerate(attendees, start=1):
        content = template
        for key in keys:
            val = attendee.get(key)
            if val is None:
                val = "N/A"
            content = content.replace(f"{{{key}}}", str(val))

        output_filename = f"output_{idx}.txt"

        try:
            with open(output_filename, "w", encoding="utf-8") as f:
                f.write(content)
        except Exception as e:
            print(f"Error writing to file {output_filename}: {e}")
