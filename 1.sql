
/*
Construa uma consulta SQL que retorne o nome, e-mail, a descrição do papel e as descrições das permissões/claims que um usuário possui.
*/

select u.name as nome,
       u.email as "e-mail",
       r.description as "descrição do papel",
       c.description as "descrições das permissões"
from users u
    INNER JOIN roles r ON u.role_id = r.id
    INNER JOIN user_claims uc ON u.id = uc.user_id
    INNER JOIN claims c ON uc.claim_id = c.id;
