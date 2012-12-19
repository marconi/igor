<!DOCTYPE html>
<html lang="en">
    <head>
        <meta charset="utf-8">
        <title>Igor</title>
    </head>
    <body>
        % if urls:
            <h1>Igor downloaded files boss :)</h1>
            <ul>
            % for url in urls:
                <li>
                    <a href="${url}">${url}</a>
                </li>
            % endfor
            </ul>
        % else:
        <h1>Igor found no files boss :(</h1>
        % endif
    </body>
</html>