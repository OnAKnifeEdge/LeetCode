/**
 * @param {string} str
 * @return {null|boolean|number|string|Array|Object}
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

