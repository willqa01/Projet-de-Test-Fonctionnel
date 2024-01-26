-- -- SELECT AVG(em.salaire) FROM departements de
-- INNER JOIN employes em ON de.departement_id = em.departement_id
-- INNER JOIN participationprojet pp ON em.employe_id = pp.employe_id
-- INNER JOIN projets pr ON pp.projet_id = pr.projet_id
-- GROUP BY de.nom_departement; 
-- SELECT AVG(em.salaire), de.nom_departement, pp.heures_travaillees, pr.budget FROM departements de
-- INNER JOIN employes em ON de.departement_id = em.departement_id
-- INNER JOIN participationprojet pp ON em.employe_id = pp.employe_id
-- INNER JOIN projets pr ON pp.projet_id = pr.projet_id
-- GROUP BY de.nom_departement
-- SELECT AVG(em.salaire) AS saliare_moyen,
--     de.nom_departement,
--     pp.heures_travaillees,
--     pr.budget
-- FROM departements de
--     INNER JOIN employes em ON de.departement_id = em.departement_id
--     INNER JOIN participationprojet pp ON em.employe_id = pp.employe_id
--     INNER JOIN projets pr ON pp.projet_id = pr.projet_id
-- GROUP BY de.nom_departement;
-- SELECT em.nom, em.prenom, de.nom_departement  FROM departements de
-- INNER JOIN employes em ON de.departement_id = em.departement_id
-- INNER JOIN participationprojet pp ON em.employe_id = pp.employe_id
-- INNER JOIN projets pr ON pp.projet_id = pr.projet_id
-- GROUP BY em.nom;
-- SELECT CONCAT(em.nom, "  " , em.prenom), de.nom_departement  FROM departements de
-- INNER JOIN employes em ON de.departement_id = em.departement_id
-- INNER JOIN participationprojet pp ON em.employe_id = pp.employe_id
-- INNER JOIN projets pr ON pp.projet_id = pr.projet_id
-- SELECT pr.nom_projet,
--     CONCAT(em.nom, "   ", em.prenom) AS nom
-- FROM departements de
--     INNER JOIN employes em ON de.departement_id = em.departement_id
--     INNER JOIN participationprojet pp ON em.employe_id = pp.employe_id
--     INNER JOIN projets pr ON pp.projet_id = pr.projet_id;
-- SELECT pr.nom_projet, CONCAT(em.nom, "   ",em.prenom) AS nom_participants FROM employes em
-- INNER JOIN participationprojet pp ON em.employe_id = pp.employe_id
-- INNER JOIN projets pr ON pp.projet_id = pr.projet_id;
-- SELECT CONCAT(em.salaire,"   ", em.nom) AS your_are_the_boss, de.nom_departement,
-- (
--         SELECT AVG(emp.salaire)
--         FROM employes emp
--         WHERE de.departement_id = emp.departement_id
--     )
-- FROM employes em
-- INNER JOIN departements de on de.departement_id = em.departement_id
-- WHERE em.salaire >
--  (
--         SELECT AVG(emp.salaire)
--         FROM employes emp
--         WHERE de.departement_id = emp.departement_id
--     );
-- SELECT CONCAT(em.salaire,"   ", em.nom) AS you_do_not_win, de.nom_departement,
-- (
--         SELECT AVG(emp.salaire)
--         FROM employes emp
--         WHERE de.departement_id = emp.departement_id
--     )
-- FROM employes em
-- INNER JOIN departements de on de.departement_id = em.departement_id
-- WHERE em.salaire <
--  (
--         SELECT AVG(emp.salaire)
--         FROM employes emp
--         WHERE de.departement_id = emp.departement_id
--     );


SELECT P.nom_projet
FROM Projets P

WHERE (

SELECT SUM(heures_travaillees)
FROM ParticipationProjet
WHERE projet_id = P.projet_id

) > (

SELECT AVG(total_heures)

FROM (

SELECT SUM(heures_travaillees) as total_heures

FROM ParticipationProjet
GROUP BY projet_id
) AS MoyenneHeures

);