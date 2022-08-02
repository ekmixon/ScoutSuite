import os
import sys


from ScoutSuite import DEFAULT_REPORT_DIRECTORY, DEFAULT_REPORT_RESULTS_DIRECTORY
from ScoutSuite.core.console import print_error


def prompt_for_yes_no(question):
    """
    Ask a question and prompt for yes or no

    :param question:                    Question to ask; answer is yes/no
    :return:                            :boolean
    """

    while True:
        sys.stdout.write(f'{question} (y/n)? ')
        choice = input().lower()
        if choice in ['yes', 'y']:
            return True
        elif choice in ['no', 'n']:
            return False
        else:
            print_error('\'%s\' is not a valid answer. Enter \'yes\'(y) or \'no\'(n).' % choice)


def prompt_for_overwrite(filename, force_write):
    """
    Confirm before overwriting existing files. Do not prompt if the file does not exist or force_write is set

    :param filename:                    Name of the file to be overwritten
    :param force_write:                 Do not ask for confirmation and automatically return True if set
    :return:                            :boolean
    """
    #
    if not os.path.exists(filename) or force_write:
        return True
    return prompt_for_yes_no(f'File \'{filename}\' already exists. Do you want to overwrite it')


def get_filename(file_type, file_name=None, file_dir=None, relative_path=False, file_extension=None):
    if file_type == 'REPORT':
        name = file_name or 'report'
        directory = file_dir or DEFAULT_REPORT_DIRECTORY
        extension = 'html'
        first_line = None
    elif file_type == 'RESULTS':
        name = f'scoutsuite_results_{file_name}' if file_name else 'scoutsuite_results'
        directory = (
            DEFAULT_REPORT_RESULTS_DIRECTORY
            if relative_path
            else os.path.join(
                file_dir or DEFAULT_REPORT_DIRECTORY,
                DEFAULT_REPORT_RESULTS_DIRECTORY,
            )
        )

        extension = 'js'
        first_line = 'scoutsuite_results ='
    elif file_type == 'EXCEPTIONS':
        name = f'scoutsuite_exceptions_{file_name}' if file_name else 'scoutsuite_exceptions'
        directory = (
            DEFAULT_REPORT_RESULTS_DIRECTORY
            if relative_path
            else os.path.join(
                file_dir or DEFAULT_REPORT_DIRECTORY,
                DEFAULT_REPORT_RESULTS_DIRECTORY,
            )
        )

        extension = 'js'
        first_line = 'exceptions ='
    elif file_type == 'ERRORS':
        name = f'scoutsuite_errors_{file_name}' if file_name else 'scoutsuite_errors'
        directory = (
            DEFAULT_REPORT_RESULTS_DIRECTORY
            if relative_path
            else os.path.join(
                file_dir or DEFAULT_REPORT_DIRECTORY,
                DEFAULT_REPORT_RESULTS_DIRECTORY,
            )
        )

        extension = 'json'
        first_line = None
    else:
        raise Exception(f'Invalid file type provided: {file_type}')

    full_path = os.path.join(directory, f'{name}.{file_extension or extension}')

    return full_path, first_line
