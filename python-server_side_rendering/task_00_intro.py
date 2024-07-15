#!/usr/bin/python3

'''
    Defines generate_invitations
'''

import os.path


def generate_invitations(template: str, attendees: list[dict]) -> None:
    '''
        Generates multiple invitations based on a template and a list of dicts
    '''

    FILE_PLACEHOLDER = "output_{:n}.txt"

    # Checks types
    if not isinstance(template, str):
        print(type(template).__name__)
        return
    if not isinstance(attendees, list):
        print(type(attendees).__name__)
        return
    for element in attendees:
        if not isinstance(element, dict):
            print(type(element).__name__)
            return
    # Checks emptiness
    if not template:
        print("Template is empty, no output files generated.")
        return
    if not attendees:
        print("No data provided, no output files generated.")
        return

    # Process attendees
    for attendee in attendees:
        output = template
        # While '{' exists replace everything until '}' included with something
        while (placeholder_start := output.find('{')) != -1:
            placeholder_end = output.find('}')
            placeholder_name = output[placeholder_start + 1: placeholder_end]
            placeholder = '{' + placeholder_name + '}'
            # Replaces with "N/A" if none
            if (placeholder_name not in attendee or
                    attendee[placeholder_name] is None):
                output = output.replace(placeholder, "N/A")
            else:
                output = output.\
                    replace(placeholder, attendee[placeholder_name])

        # Rename to shorten code
        def generatePath(num):
            return FILE_PLACEHOLDER.format(num)
        # Generates number for file
        number_of_file = 1
        while os.path.exists(generatePath(number_of_file)):
            number_of_file += 1
        # Writes to file
        with open(generatePath(number_of_file), '+w') as f:
            f.write(output)
