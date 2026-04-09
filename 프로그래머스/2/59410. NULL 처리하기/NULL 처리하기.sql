-- 코드를 입력하세요
SELECT ANIMAL_TYPE,
    case
        when NAME is null then "No name"
        else NAME
    end as NAME, SEX_UPON_INTAKE
from animal_ins
order by animal_id
