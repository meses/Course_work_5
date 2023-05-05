--Создание таблицы Компании
CREATE TABLE public.employers (
	id integer NOT NULL,
	"name" varchar(256) NULL,
	url varchar(256) NULL,
	description text NULL
	CONSTRAINT employers_pk PRIMARY KEY (id)
);
COMMENT ON TABLE public.employers IS 'Компании';

--Создание таблицы Вакансия
CREATE TABLE public.vacancy (
	id int4 NOT NULL,
	"name" varchar(256) NULL,
	salary_from int4 NULL,
	salary_to int4 NULL,
	emlployer_id int4 NOT NULL,
	url varchar(256) NULL,
	currency varchar(64) NULL,
	requirement text NULL,
	responsibility text NULL
);
COMMENT ON TABLE public.vacancy IS 'Вакансия';
ALTER TABLE public.vacancy ADD CONSTRAINT vacancy_pk PRIMARY KEY (id);
ALTER TABLE public.vacancy ADD CONSTRAINT vacancy_fk FOREIGN KEY (emlployer_id) REFERENCES public.employers(id) ON DELETE CASCADE ON UPDATE CASCADE;
