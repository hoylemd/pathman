def detail_url(identifier, pattern, prefix='', extension=''):
    """
    Generates a url regex based on the passed identifier column name
    and the expected pattern.

    :param identifier: The model field used to select the record
        (e.g. 'pk' or 'slug')
    :type identifier: string

    :param pattern: Regular expression pattern for identifiers
    :type pattern: string or regexp

    :param prefix: Optional prefix on the url before the identifier
    :type prefix: string or regexp

    :rtype: a detail url pattern
    """
    suffix = extension if extension else '/?'
    return r'^{}(?P<{}>{}){}$'.format(prefix, identifier, pattern, suffix)


def slug_url(prefix='', extension=''):
    return detail_url('slug', '[a-z0-9\-_]+',
                      prefix=prefix, extension=extension)
