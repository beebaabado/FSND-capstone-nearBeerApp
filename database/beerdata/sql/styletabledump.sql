--
-- PostgreSQL database dump
--

-- Dumped from database version 13.2
-- Dumped by pg_dump version 13.2

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

--
-- Data for Name: style; Type: TABLE DATA; Schema: public; Owner: postgres
--

INSERT INTO public.style (id, major, sub_styles) VALUES (15, 'IPA', 'IPA');
INSERT INTO public.style (id, major, sub_styles) VALUES (16, 'Stout', 'Stout,Schwarzbier');
INSERT INTO public.style (id, major, sub_styles) VALUES (17, 'Sour', 'Sour,Gose');
INSERT INTO public.style (id, major, sub_styles) VALUES (18, 'Wheat', 'Wheat,Hefeweisen,Witbier,Weizen,Grätzer');
INSERT INTO public.style (id, major, sub_styles) VALUES (19, 'Ale', 'Ale,Barleywine,Kölsch');
INSERT INTO public.style (id, major, sub_styles) VALUES (20, 'Porter', 'Porter');
INSERT INTO public.style (id, major, sub_styles) VALUES (21, 'Cider', 'Cider');
INSERT INTO public.style (id, major, sub_styles) VALUES (22, 'Hard Seltzer', 'Hard Seltzer');
INSERT INTO public.style (id, major, sub_styles) VALUES (23, 'Belgian', 'Belgian, Lambic');
INSERT INTO public.style (id, major, sub_styles) VALUES (24, 'Lager', 'Lager,Bock,Pilsner,Altbier,Märzen,Kellerbier');
INSERT INTO public.style (id, major, sub_styles) VALUES (25, 'Mead', 'Mead');
INSERT INTO public.style (id, major, sub_styles) VALUES (26, 'Gluten Free', 'Gluten Free,GF,Kombucha');
INSERT INTO public.style (id, major, sub_styles) VALUES (27, 'Non-Alcoholic', 'Non-Alcoholic');
INSERT INTO public.style (id, major, sub_styles) VALUES (28, 'Other', 'Other');


--
-- Name: style_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.style_id_seq', 28, true);


--
-- PostgreSQL database dump complete
--

