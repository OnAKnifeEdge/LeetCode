/**
 * @param {string} str
 * @return {null|boolean|number|string|Array|Object}
 */



/**
python version
def parse_json(s: str):
    i = 0

    def parse_value():
        nonlocal i
        if s[i] == '{': return parse_object()
        if s[i] == '[': return parse_array()
        if s[i] == '"': return parse_string()
        if s[i] == 't': return parse_true()
        if s[i] == 'f': return parse_false()
        if s[i] == 'n': return parse_null()
        return parse_number()

    def parse_object():
        nonlocal i
        obj = {}
        i += 1
        while s[i] != '}':
            key = parse_string()
            i += 1  # Skip colon
            obj[key] = parse_value()
            if s[i] == ',': i += 1
        i += 1
        return obj

    def parse_array():
        nonlocal i
        arr = []
        i += 1
        while s[i] != ']':
            arr.append(parse_value())
            if s[i] == ',': i += 1
        i += 1
        return arr

    def parse_string():
        nonlocal i
        result = ''
        i += 1
        while s[i] != '"':
            result += s[i]
            i += 1
        i += 1
        return result

    def parse_number():
        nonlocal i
        num_str = ''
        while i < len(s) and (s[i].isdigit() or s[i] in '.-'):
            num_str += s[i]
            i += 1
        return float(num_str) if '.' in num_str else int(num_str)

    def parse_true():
        nonlocal i
        i += 4
        return True

    def parse_false():
        nonlocal i
        i += 5
        return False

    def parse_null():
        nonlocal i
        i += 4
        return None

    return parse_value()
 */
var jsonParse = function (str) {
    let i = 0;

    function parseValue() {
        if (str[i] === '{') return parseObject();
        if (str[i] === '[') return parseArray();
        if (str[i] === '"') return parseString();
        if (str[i] === 't') return parseTrue();
        if (str[i] === 'f') return parseFalse();
        if (str[i] === 'n') return parseNull();
        return parseNumber();
    }

    function parseObject() {
        const obj = {};
        i++;
        while (str[i] !== '}') {
            const key = parseString();
            i++; // Skip colon
            obj[key] = parseValue();
            if (str[i] === ',') i++;
        }
        i++;
        return obj;
    }

    function parseArray() {
        const arr = [];
        i++;
        while (str[i] !== ']') {
            arr.push(parseValue());
            if (str[i] === ',') i++;
        }
        i++;
        return arr;
    }

    function parseString() {
        let result = '';
        i++;
        while (str[i] !== '"') {
            result += str[i++];
        }
        i++;
        return result;
    }

    function parseNumber() {
        let numStr = '';
        while (str[i] >= '0' && str[i] <= '9' || str[i] === '.' || str[i] === '-') {
            numStr += str[i++];
        }
        return parseFloat(numStr);
    }

    function parseTrue() {
        i += 4;
        return true;
    }

    function parseFalse() {
        i += 5;
        return false;
    }

    function parseNull() {
        i += 4;
        return null;
    }

    return parseValue();
};

