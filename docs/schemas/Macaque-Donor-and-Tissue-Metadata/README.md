# BICAN Macaque Donor and Tissue Metadata Schema

Document Status: _Accepted by MOWG_

Version: 1.0

Owner: HMBA

Reviewers: @mgiglio99, @puja-trivedi, @patrick-lloyd-ray

License: [CC-BY-4.0](https://creativecommons.org/licenses/by/4.0/)

Date Created: 08-07-2024

## Background

The Brain Research Through Advancing Innovative Neurotechnologies® (BRAIN) Initiative Cell Atlas Network (BICAN) aims to transform our understanding of brain cell types and the precise tools needed to access them, bringing us one step closer to unraveling the complex workings of the human brain.

Building on findings from the BRAIN Initiative Cell Census Network (BICCN), BICAN takes the next step in mapping brain cells and circuits across multiple species, with an emphasis on humans. The aim of BICAN is to generate a complete reference atlas of cell types in the human brain across the lifespan, which can be shared and used throughout the research community. In addition to developing a “parts list” detailing the vast array of neurons and non-neuronal cells in the human brain, the project also aims to map cell interactions that underlie a wide range of brain disorders.

To this end, BICAN aims to support the publication, sharing, and exploration of datasets generated in the course of the project. Creating a complete reference atlas from multiple datasets requires vast harmonization of metadata. In order to facilitate the harmonization of metadata, we require datasets include a small set of metadata available from data submitters.

This document describes a schema, a type of contract, that BICAN requires of all donor to alignment datasets to enable searching, filtering, and integration of datasets.

Note that the requirements in the schema are just the minimum required information. Datasets often have additional metadata, which is preserved in datasets submitted to the data archives.

## Overview

The BICAN Macaque Donor and Tissue Metadata schema describes metadata associated with and produced from the preparation of macaque donor and tissue in the HMBA and BICAN. [more detail needed here]

This document has the following sections:

* [General Requirements](#general-requirements)
* [PatchSeq](#patchseq), which describe the metadata required for macaque patchseq experiments.
* [Population](#population), which describe the metadata required for macaque population studies.
* [Whole Brain Spatial Omics](#whole-brain-spatial-omics), which describe the metadata required for whole brain spatial omics experiements.
* [Appendix](#appendix)

## General Requirements

**Organisms**. Data must be from a Metazoan organism and defined in the NCBI organismal classification.

**Redundant Metadata**. It is STRONGLY RECOMMENDED to avoid multiple metadata fields containing identical or similar information.

## PatchSeq

The data in patchseq is the metadata essential for macaque patchseq experiments.

The following tables describe the patchseq metadata. If an entry in the table is empty, the schema does not have any other requirements on data in those layers beyond the ones listed above.

Curators must annotate the following columns:

### Local Donor ID

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td>local donor ID</td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td>f8af20f7-e8b8-47b5-8a68-9ec1f913ffdf</td>
    </tr>
    <tr>
      <th>Definition</th>
      <td>An identifier that uniquely denotes objects only within the scope of a specific object aggregate and that is not registered in an identifier registry.</td>
    </tr>
    <tr>
      <th>Aliases</th>
      <td>subject_id</td>
    </tr>
    <tr>
      <th>Data Type</th>
      <td>text</td>
    </tr>
</tbody></table>
<br>

### Repository

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td>repository</td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td>408682ed-0e27-41e2-b9fa-f05674366d6e</td>
    </tr>
    <tr>
      <th>Definition</th>
      <td>'Repository' trailing modifier (qualifier, 'repository') of 'xref' links of 'Format' concepts. When 'true', the link is pointing to the public source-code repository where the given data format is developed or maintained.</td>
    </tr>
    <tr>
      <th>Aliases</th>
      <td>repository</td>
    </tr>
    <tr>
      <th>Data Type</th>
      <td>inclusive_categorical</td>
    </tr>
</tbody></table>
<br>

### Donor Source

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td>donor source</td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td>0d0cf732-0f76-409d-9a73-7a96d829d3d3</td>
    </tr>
    <tr>
      <th>Definition</th>
      <td>The origin of the donor/subject in this experiment.</td>
    </tr>
    <tr>
      <th>Aliases</th>
      <td>donor_source</td>
    </tr>
    <tr>
      <th>Data Type</th>
      <td>inclusive_categorical</td>
    </tr>
</tbody></table>
<br>

### Sex at Birth

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td>sex at birth</td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td>c819b9d5-2fde-40b2-bf0d-e07b56f96ac9</td>
    </tr>
    <tr>
      <th>Definition</th>
      <td>An organismal quality inhering in a bearer by virtue of the bearer's ability to undergo sexual reproduction in order to differentiate the individuals or types involved.</td>
    </tr>
    <tr>
      <th>Aliases</th>
      <td>sex</td>
    </tr>
    <tr>
      <th>Data Type</th>
      <td>exclusive_categorical</td>
    </tr>
</tbody></table>
<br>

### Age Value (Years)

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td>age value (years)</td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td>14eb923a-161d-45e2-889d-81fea7b632b6</td>
    </tr>
    <tr>
      <th>Definition</th>
      <td>A time quality inhering in a bearer by virtue of how long the bearer has existed.</td>
    </tr>
    <tr>
      <th>Aliases</th>
      <td>age_of_death</td>
    </tr>
    <tr>
      <th>Data Type</th>
      <td>numeric</td>
    </tr>
</tbody></table>
<br>

### Year of Death

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td>year of death</td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td>60445046-d9d8-4f00-959e-9a4c42613e5e</td>
    </tr>
    <tr>
      <th>Definition</th>
      <td>The year wherein the subject or donor has ceased to exist.</td>
    </tr>
    <tr>
      <th>Aliases</th>
      <td>year_of_death</td>
    </tr>
    <tr>
      <th>Data Type</th>
      <td>date</td>
    </tr>
</tbody></table>
<br>

### Manner of Death

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td>manner of death</td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td>36eeb35b-5020-4a9e-a74b-6e1104415e0e</td>
    </tr>
    <tr>
      <th>Definition</th>
      <td>The manner of death is the determination of how the injury or disease leads to death.  There are five manners of death (natural, accident, suicide, homicide, and undetermined).</td>
    </tr>
    <tr>
      <th>Aliases</th>
      <td>manner_of_death</td>
    </tr>
    <tr>
      <th>Data Type</th>
      <td>exclusive_categorical</td>
    </tr>
</tbody></table>
<br>

### Medical Records Available

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td>medical records available</td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td>ee2c9223-f7d1-4c64-a1da-cd7408309955</td>
    </tr>
    <tr>
      <th>Definition</th>
      <td>The status (available, unavailable) of the medical records of the subject/donor.</td>
    </tr>
    <tr>
      <th>Aliases</th>
      <td>medical_records_available</td>
    </tr>
    <tr>
      <th>Data Type</th>
      <td>exclusive_categorical</td>
    </tr>
</tbody></table>
<br>

### Medical Records Reviewed

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td>medical records reviewed</td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td>6139b159-c36c-4501-9176-fe2741e3d448</td>
    </tr>
    <tr>
      <th>Definition</th>
      <td>The status (reviewed, not reviewed) of the medical records of the subject/donor.</td>
    </tr>
    <tr>
      <th>Aliases</th>
      <td>medical_records_reviewed</td>
    </tr>
    <tr>
      <th>Data Type</th>
      <td>exclusive_categorical</td>
    </tr>
</tbody></table>
<br>

### Hemisphere

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td>hemisphere</td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td>68b7a28b-d695-4ec9-800b-6a27ca206081</td>
    </tr>
    <tr>
      <th>Definition</th>
      <td>One of two bilateral, largely symmetrical organ subdivisions within the telencephalon which contain the cerebral cortex and cerebral white matter.</td>
    </tr>
    <tr>
      <th>Aliases</th>
      <td>hemisphere</td>
    </tr>
    <tr>
      <th>Data Type</th>
      <td>exclusive_categorical</td>
    </tr>
</tbody></table>
<br>

### Post Mortem Interval

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td>post mortem interval</td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td>6fd5c5ac-b128-4a4a-ae98-09eaeba22f92</td>
    </tr>
    <tr>
      <th>Definition</th>
      <td>The length of the temporal interval between the time of death of the subject/donor and the time at which the specimen is made.</td>
    </tr>
    <tr>
      <th>Aliases</th>
      <td>post_mortem_interval</td>
    </tr>
    <tr>
      <th>Data Type</th>
      <td>numeric</td>
    </tr>
</tbody></table>
<br>

### Left Hemisphere Preparation

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td>left hemisphere preparation</td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td>57d5378f-a451-4bf5-a472-cc88d0d29586</td>
    </tr>
    <tr>
      <th>Definition</th>
      <td>The type of preparation method used for the left hemisphere.</td>
    </tr>
    <tr>
      <th>Aliases</th>
      <td>left_hemisphere_preparation</td>
    </tr>
    <tr>
      <th>Data Type</th>
      <td>exclusive_categorical</td>
    </tr>
</tbody></table>
<br>

### Left Hemisphere Preparation Specify

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td>left hemisphere preparation specify</td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td>002e915e-01c3-4570-a1f3-76680dcb2c33</td>
    </tr>
    <tr>
      <th>Definition</th>
      <td>Specific details about the type of preparation method used for the left hemisphere.</td>
    </tr>
    <tr>
      <th>Aliases</th>
      <td>left_hemisphere_preparation_specify</td>
    </tr>
    <tr>
      <th>Data Type</th>
      <td>text</td>
    </tr>
</tbody></table>
<br>

### Right Hemisphere Preparation

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td>right hemisphere preparation</td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td>477c2600-f979-43c5-9c61-ab61fd771584</td>
    </tr>
    <tr>
      <th>Definition</th>
      <td>The type of preparation method used for the right hemisphere.</td>
    </tr>
    <tr>
      <th>Aliases</th>
      <td>right_hemisphere_preparation</td>
    </tr>
    <tr>
      <th>Data Type</th>
      <td>exclusive_categorical</td>
    </tr>
</tbody></table>
<br>

### Right Hemisphere Preparation Specify

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td>right hemisphere preparation specify</td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td>efd50be4-f7cf-4146-a08e-28f25680728c</td>
    </tr>
    <tr>
      <th>Definition</th>
      <td>Specific details about the type of preparation method used for the right hemisphere.</td>
    </tr>
    <tr>
      <th>Aliases</th>
      <td>right_hemisphere_preparation_specify</td>
    </tr>
    <tr>
      <th>Data Type</th>
      <td>text</td>
    </tr>
</tbody></table>
<br>

### Photo 2D Available

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td>photo 2d available</td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td>611beda8-1ac6-4183-a284-04a30bb474f3</td>
    </tr>
    <tr>
      <th>Definition</th>
      <td>The status (available, unavailable) of two-dimensional photos of a subject/donor/specimen.</td>
    </tr>
    <tr>
      <th>Aliases</th>
      <td>photo_2d_available</td>
    </tr>
    <tr>
      <th>Data Type</th>
      <td>exclusive_categorical</td>
    </tr>
</tbody></table>
<br>

### Antemortem MRI Available

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td>antemortem MRI available</td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td>43a04caa-4f28-47ac-8a9d-74c40f10776f</td>
    </tr>
    <tr>
      <th>Definition</th>
      <td>The status (available, unavailable) of antemortem MRI images of a subject/donor/specimen.</td>
    </tr>
    <tr>
      <th>Aliases</th>
      <td>antemortem_mri_available</td>
    </tr>
    <tr>
      <th>Data Type</th>
      <td>exclusive_categorical</td>
    </tr>
</tbody></table>
<br>

### Non-Brain Tissue Available

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td>non-brain tissue available</td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td>3a064c96-a956-4cf3-8b77-056b8e392f99</td>
    </tr>
    <tr>
      <th>Definition</th>
      <td>The status (yes, no) of whether non-brain tissue from this organism is available.</td>
    </tr>
    <tr>
      <th>Aliases</th>
      <td>non_brain_tissue_available</td>
    </tr>
    <tr>
      <th>Data Type</th>
      <td>exclusive_categorical</td>
    </tr>
</tbody></table>
<br>

### Tissue Type

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td>tissue type</td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td>33ccbc85-ae35-44d6-8bc6-c2fb91116cf7</td>
    </tr>
    <tr>
      <th>Definition</th>
      <td>The type of tissue (non-brain) that is available from this organism. </td>
    </tr>
    <tr>
      <th>Aliases</th>
      <td>tissue_type</td>
    </tr>
    <tr>
      <th>Data Type</th>
      <td>exclusive_categorical</td>
    </tr>
</tbody></table>
<br>

### Tissue Type Details

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td>tissue type details</td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td>f551cf87-2c6e-4b92-888d-6310e6a500d8</td>
    </tr>
    <tr>
      <th>Definition</th>
      <td>The details of the non-brain tissue that is available from this organism.</td>
    </tr>
    <tr>
      <th>Aliases</th>
      <td>tissue_type_details</td>
    </tr>
    <tr>
      <th>Data Type</th>
      <td>text</td>
    </tr>
</tbody></table>
<br>

### Test Name

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td>test name</td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td>b6865e15-7538-4890-be99-a6f9e9920af3</td>
    </tr>
    <tr>
      <th>Definition</th>
      <td>The name of the test that has been performed.</td>
    </tr>
    <tr>
      <th>Aliases</th>
      <td>test_name</td>
    </tr>
    <tr>
      <th>Data Type</th>
      <td>exclusive_categorical</td>
    </tr>
</tbody></table>
<br>

### Result

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td>test result</td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td>c14ea006-662c-4666-bfd1-6ff580c403ed</td>
    </tr>
    <tr>
      <th>Definition</th>
      <td>The result(s) of the test that has been performed.</td>
    </tr>
    <tr>
      <th>Aliases</th>
      <td>test_result</td>
    </tr>
    <tr>
      <th>Data Type</th>
      <td>exclusive_categorical</td>
    </tr>
</tbody></table>
<br>

### Testing Tissue Source

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td>testing tissue source</td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td>42f8e11b-d9a3-48fe-ac1e-cd6f4469de46</td>
    </tr>
    <tr>
      <th>Definition</th>
      <td>The tissue sample location or identifier that is the subject of a test. </td>
    </tr>
    <tr>
      <th>Aliases</th>
      <td>tissue_source</td>
    </tr>
    <tr>
      <th>Data Type</th>
      <td>exclusive_categorical</td>
    </tr>
</tbody></table>
<br>

### Species

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td>species</td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td>d11fb2ce-bfdb-4735-9b17-b6ba606520b1</td>
    </tr>
    <tr>
      <th>Definition</th>
      <td>The species of a subject/donor/sample/specimen.</td>
    </tr>
    <tr>
      <th>Aliases</th>
      <td>species</td>
    </tr>
    <tr>
      <th>Data Type</th>
      <td>exclusive_categorical</td>
    </tr>
</tbody></table>
<br>

### Premortem perfusion done

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td>premortem perfusion done</td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td>1fc487d8-2403-4d7c-952f-7e502d5f8359</td>
    </tr>
    <tr>
      <th>Definition</th>
      <td>The status of premortem perfusion (done, not done).</td>
    </tr>
    <tr>
      <th>Aliases</th>
      <td>perfusion</td>
    </tr>
    <tr>
      <th>Data Type</th>
      <td>exclusive_categorical</td>
    </tr>
</tbody></table>
<br>

### Premortem perfusion buffer type

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td>premortem perfusion buffer type</td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td>78d62e29-4323-4927-aec8-6fc8dc59a889</td>
    </tr>
    <tr>
      <th>Definition</th>
      <td>The type of premortem perfusion buffer that was used for premortem perfusion. </td>
    </tr>
    <tr>
      <th>Aliases</th>
      <td>perfusate_type</td>
    </tr>
    <tr>
      <th>Data Type</th>
      <td>text</td>
    </tr>
</tbody></table>
<br>

### Region of interest

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td>region of interest</td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td>71611b58-f98e-4a69-ad88-c0029a377cbe</td>
    </tr>
    <tr>
      <th>Definition</th>
      <td>The brain region, structure, or area from which a brain tissue source derives.</td>
    </tr>
    <tr>
      <th>Aliases</th>
      <td>ROI</td>
    </tr>
    <tr>
      <th>Data Type</th>
      <td>exclusive_categorical</td>
    </tr>
</tbody></table>
<br>

### Behavorial Testing

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td>behavioral scoring available</td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td>ea33881a-9813-4111-979b-135355e8141e</td>
    </tr>
    <tr>
      <th>Definition</th>
      <td>The status (available, unavailable) of the behavioral scoring results for a subject/donor/specimen.</td>
    </tr>
    <tr>
      <th>Aliases</th>
      <td>behavioral_scoring_available</td>
    </tr>
    <tr>
      <th>Data Type</th>
      <td>exclusive_categorical</td>
    </tr>
</tbody></table>
<br>

### Behavorial Testing Type

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td>behavioral scoring type</td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td>0a7a1eeb-8682-4261-8221-82d587dde0fa</td>
    </tr>
    <tr>
      <th>Definition</th>
      <td>The type of behavioral scoring that is available for a subject/donor/specimen.</td>
    </tr>
    <tr>
      <th>Aliases</th>
      <td>behavioral_scoring_type</td>
    </tr>
    <tr>
      <th>Data Type</th>
      <td>text</td>
    </tr>
</tbody></table>
<br>

### Non Brain Diagnosis Description

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td>non brain diagnosis description</td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td>4ba7c8cc-563c-4f0b-ab57-ae9c9762943f</td>
    </tr>
    <tr>
      <th>Definition</th>
      <td>The description (text) of a non-brain diagnosis for a subject/donor/specimen.</td>
    </tr>
    <tr>
      <th>Aliases</th>
      <td>non_brain_diagnosis_description</td>
    </tr>
    <tr>
      <th>Data Type</th>
      <td>text</td>
    </tr>
</tbody></table>
<br>

## Population

The data in population is the metadata essential for macaque population studies.

The following tables describe the population metadata. If an entry in the table is empty, the schema does not have any other requirements on data in those layers beyond the ones listed above.

Curators must annotate the following columns:

### Local Donor ID

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td>local donor ID</td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td>f8af20f7-e8b8-47b5-8a68-9ec1f913ffdf</td>
    </tr>
    <tr>
      <th>Definition</th>
      <td></td>
    </tr>
    <tr>
      <th>Aliases</th>
      <td>subject_id</td>
    </tr>
    <tr>
      <th>Data Type</th>
      <td>text</td>
    </tr>
</tbody></table>
<br>

### Repository

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td>repository</td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td>408682ed-0e27-41e2-b9fa-f05674366d6e</td>
    </tr>
    <tr>
      <th>Definition</th>
      <td>'Repository' trailing modifier (qualifier, 'repository') of 'xref' links of 'Format' concepts. When 'true', the link is pointing to the public source-code repository where the given data format is developed or maintained.</td>
    </tr>
    <tr>
      <th>Aliases</th>
      <td>repository</td>
    </tr>
    <tr>
      <th>Data Type</th>
      <td>inclusive_categorical</td>
    </tr>
</tbody></table>
<br>

### Donor Source

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td>donor source</td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td>0d0cf732-0f76-409d-9a73-7a96d829d3d3</td>
    </tr>
    <tr>
      <th>Definition</th>
      <td>The origin of the donor/subject in this experiment.</td>
    </tr>
    <tr>
      <th>Aliases</th>
      <td>donor_source</td>
    </tr>
    <tr>
      <th>Data Type</th>
      <td>inclusive_categorical</td>
    </tr>
</tbody></table>
<br>

### Sex at Birth

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td>sex at birth</td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td>c819b9d5-2fde-40b2-bf0d-e07b56f96ac9</td>
    </tr>
    <tr>
      <th>Definition</th>
      <td>An organismal quality inhering in a bearer by virtue of the bearer's ability to undergo sexual reproduction in order to differentiate the individuals or types involved.</td>
    </tr>
    <tr>
      <th>Aliases</th>
      <td>sex</td>
    </tr>
    <tr>
      <th>Data Type</th>
      <td>exclusive_categorical</td>
    </tr>
</tbody></table>
<br>

### Age Value (Years)

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td>age value (years)</td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td>14eb923a-161d-45e2-889d-81fea7b632b6</td>
    </tr>
    <tr>
      <th>Definition</th>
      <td>A time quality inhering in a bearer by virtue of how long the bearer has existed.</td>
    </tr>
    <tr>
      <th>Aliases</th>
      <td>age_of_death</td>
    </tr>
    <tr>
      <th>Data Type</th>
      <td>numeric</td>
    </tr>
</tbody></table>
<br>

### Year of Death

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td>year of death</td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td>60445046-d9d8-4f00-959e-9a4c42613e5e</td>
    </tr>
    <tr>
      <th>Definition</th>
      <td>The year wherein the subject or donor has ceased to exist.</td>
    </tr>
    <tr>
      <th>Aliases</th>
      <td>year_of_death</td>
    </tr>
    <tr>
      <th>Data Type</th>
      <td>date</td>
    </tr>
</tbody></table>
<br>

### Autopsy Report

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td>autopsy report</td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td>3f787b64-0985-4d0f-9523-54475164b7ad</td>
    </tr>
    <tr>
      <th>Definition</th>
      <td>A document assembled by an author for the purpose of providing information regarding the cause of death of a subject for the audience.</td>
    </tr>
    <tr>
      <th>Aliases</th>
      <td>autopsy_report</td>
    </tr>
    <tr>
      <th>Data Type</th>
      <td>exclusive_categorical</td>
    </tr>
</tbody></table>
<br>

### Cause of Death

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td>cause of death</td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td>fa970a03-41ea-473b-a8ce-427fec92cdff</td>
    </tr>
    <tr>
      <th>Definition</th>
      <td>The circumstance or condition that results in the death of a living being. [NCIT]</td>
    </tr>
    <tr>
      <th>Aliases</th>
      <td>cause_of_death</td>
    </tr>
    <tr>
      <th>Data Type</th>
      <td>text</td>
    </tr>
</tbody></table>
<br>

### Cause of Death Code

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td>cause of death code</td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td>61374624-2d3c-477e-95b3-9bd30974b52a</td>
    </tr>
    <tr>
      <th>Definition</th>
      <td>The ISO code that denotes the circumstance or condition that results in the death of a living being.</td>
    </tr>
    <tr>
      <th>Aliases</th>
      <td>cause_of_death_code</td>
    </tr>
    <tr>
      <th>Data Type</th>
      <td>text</td>
    </tr>
</tbody></table>
<br>

### Manner of Death

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td>manner of death</td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td>36eeb35b-5020-4a9e-a74b-6e1104415e0e</td>
    </tr>
    <tr>
      <th>Definition</th>
      <td>The manner of death is the determination of how the injury or disease leads to death.  There are five manners of death (natural, accident, suicide, homicide, and undetermined).</td>
    </tr>
    <tr>
      <th>Aliases</th>
      <td>manner_of_death</td>
    </tr>
    <tr>
      <th>Data Type</th>
      <td>exclusive_categorical</td>
    </tr>
</tbody></table>
<br>

### Medical Records Reviewed

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td>medical records reviewed</td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td>6139b159-c36c-4501-9176-fe2741e3d448</td>
    </tr>
    <tr>
      <th>Definition</th>
      <td>The status (reviewed, not reviewed) of the medical records of the subject/donor.</td>
    </tr>
    <tr>
      <th>Aliases</th>
      <td>medical_records_reviewed</td>
    </tr>
    <tr>
      <th>Data Type</th>
      <td>exclusive_categorical</td>
    </tr>
</tbody></table>
<br>

### Hemisphere

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td>hemisphere</td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td>68b7a28b-d695-4ec9-800b-6a27ca206081</td>
    </tr>
    <tr>
      <th>Definition</th>
      <td>One of two bilateral, largely symmetrical organ subdivisions within the telencephalon which contain the cerebral cortex and cerebral white matter.</td>
    </tr>
    <tr>
      <th>Aliases</th>
      <td>hemisphere</td>
    </tr>
    <tr>
      <th>Data Type</th>
      <td>exclusive_categorical</td>
    </tr>
</tbody></table>
<br>

### Post Mortem Interval

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td>post mortem interval</td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td>6fd5c5ac-b128-4a4a-ae98-09eaeba22f92</td>
    </tr>
    <tr>
      <th>Definition</th>
      <td>The length of the temporal interval between the time of death of the subject/donor and the time at which the specimen is made.</td>
    </tr>
    <tr>
      <th>Aliases</th>
      <td>post_mortem_interval</td>
    </tr>
    <tr>
      <th>Data Type</th>
      <td>numeric</td>
    </tr>
</tbody></table>
<br>

### Left Hemisphere Preparation

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td>left hemisphere preparation</td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td>57d5378f-a451-4bf5-a472-cc88d0d29586</td>
    </tr>
    <tr>
      <th>Definition</th>
      <td>The type of preparation method used for the left hemisphere.</td>
    </tr>
    <tr>
      <th>Aliases</th>
      <td>left_hemisphere_preparation</td>
    </tr>
    <tr>
      <th>Data Type</th>
      <td>exclusive_categorical</td>
    </tr>
</tbody></table>
<br>

### Left Hemisphere Preparation Specify

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td>left hemisphere preparation specify</td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td>002e915e-01c3-4570-a1f3-76680dcb2c33</td>
    </tr>
    <tr>
      <th>Definition</th>
      <td>Specific details about the type of preparation method used for the left hemisphere.</td>
    </tr>
    <tr>
      <th>Aliases</th>
      <td>left_hemisphere_preparation_specify</td>
    </tr>
    <tr>
      <th>Data Type</th>
      <td>text</td>
    </tr>
</tbody></table>
<br>

### Right Hemisphere Preparation

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td>right hemisphere preparation</td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td>477c2600-f979-43c5-9c61-ab61fd771584</td>
    </tr>
    <tr>
      <th>Definition</th>
      <td>The type of preparation method used for the right hemisphere.</td>
    </tr>
    <tr>
      <th>Aliases</th>
      <td>right_hemisphere_preparation</td>
    </tr>
    <tr>
      <th>Data Type</th>
      <td>exclusive_categorical</td>
    </tr>
</tbody></table>
<br>

### Right Hemisphere Preparation Specify

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td>right hemisphere preparation specify</td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td>efd50be4-f7cf-4146-a08e-28f25680728c</td>
    </tr>
    <tr>
      <th>Definition</th>
      <td>Specific details about the type of preparation method used for the right hemisphere.</td>
    </tr>
    <tr>
      <th>Aliases</th>
      <td>right_hemisphere_preparation_specify</td>
    </tr>
    <tr>
      <th>Data Type</th>
      <td>text</td>
    </tr>
</tbody></table>
<br>

### RIN

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td>RIN</td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td>cd472c0d-0b64-45c9-a38e-e54d15cea953</td>
    </tr>
    <tr>
      <th>Definition</th>
      <td>The RNA integrity number value of a specimen.</td>
    </tr>
    <tr>
      <th>Aliases</th>
      <td>rin</td>
    </tr>
    <tr>
      <th>Data Type</th>
      <td>numeric</td>
    </tr>
</tbody></table>
<br>

### RIN Tissue Source

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td>RIN tissue source</td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td>d547ee51-9ec3-489c-8e49-7d8cd94080a8</td>
    </tr>
    <tr>
      <th>Definition</th>
      <td>The tissue sample location or identifier that is used for calculating the RNA integrity number.</td>
    </tr>
    <tr>
      <th>Aliases</th>
      <td>rin_tissue_source</td>
    </tr>
    <tr>
      <th>Data Type</th>
      <td>text</td>
    </tr>
</tbody></table>
<br>

### RIN Testing Organization

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td>RIN testing organization</td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td>cfed831e-9a62-4a32-bf92-532873420eb3</td>
    </tr>
    <tr>
      <th>Definition</th>
      <td>The organization that determines the RNA integrity number of a sample/specimen.</td>
    </tr>
    <tr>
      <th>Aliases</th>
      <td>rin_testing_organization</td>
    </tr>
    <tr>
      <th>Data Type</th>
      <td>text</td>
    </tr>
</tbody></table>
<br>

### RINe

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td>RINe</td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td>1210148d-d8fb-45aa-b51a-4b19b6d09bec</td>
    </tr>
    <tr>
      <th>Definition</th>
      <td>A type of RIN (RNA integrity number) value that represents the relative ratio of the signal in the fast zone to the 18S peak signal fpr a specimen.</td>
    </tr>
    <tr>
      <th>Aliases</th>
      <td>rine</td>
    </tr>
    <tr>
      <th>Data Type</th>
      <td>numeric</td>
    </tr>
</tbody></table>
<br>

### RINe Tissue Source

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td>RINe tissue source</td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td>7d5fd9af-82a1-4bdb-a3c6-9225d1717c53</td>
    </tr>
    <tr>
      <th>Definition</th>
      <td>The tissue sample location or identifier that is used for calculating the RINe number.</td>
    </tr>
    <tr>
      <th>Aliases</th>
      <td>rine_tissue_source</td>
    </tr>
    <tr>
      <th>Data Type</th>
      <td>text</td>
    </tr>
</tbody></table>
<br>

### RINe Testing Organization

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td>RINe testing organization</td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td>15a6d162-a3ca-4852-b626-a911c37c04c9</td>
    </tr>
    <tr>
      <th>Definition</th>
      <td>The organization that determines the RINe number.</td>
    </tr>
    <tr>
      <th>Aliases</th>
      <td>rine_testing_organization</td>
    </tr>
    <tr>
      <th>Data Type</th>
      <td>text</td>
    </tr>
</tbody></table>
<br>

### pH

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td>pH</td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td>9e67af02-c081-43e1-a42c-bf9603cae616</td>
    </tr>
    <tr>
      <th>Definition</th>
      <td>The value of a measurement of acidity or basicity of a tissue, sample, or specimen.</td>
    </tr>
    <tr>
      <th>Aliases</th>
      <td>ph</td>
    </tr>
    <tr>
      <th>Data Type</th>
      <td>numeric</td>
    </tr>
</tbody></table>
<br>

### Brain Weight

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td>brain weight measurement</td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td>546fc32d-f8a2-4c00-924a-8c4730f11f51</td>
    </tr>
    <tr>
      <th>Definition</th>
      <td>The weight of a brain specimen.</td>
    </tr>
    <tr>
      <th>Aliases</th>
      <td>brain_weight</td>
    </tr>
    <tr>
      <th>Data Type</th>
      <td>numeric</td>
    </tr>
</tbody></table>
<br>

### Brain Tissue Weighed Type

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td>brain tissue weighed type</td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td>a7463e3f-0c61-4718-a7d0-60fd2116908a</td>
    </tr>
    <tr>
      <th>Definition</th>
      <td>The state of a brain specimen when it is weighed (fresh, frozen, fixed).</td>
    </tr>
    <tr>
      <th>Aliases</th>
      <td>weighed_type</td>
    </tr>
    <tr>
      <th>Data Type</th>
      <td>exclusive_categorical</td>
    </tr>
</tbody></table>
<br>

### Photo 2D Available

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td>photo 2d available</td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td>611beda8-1ac6-4183-a284-04a30bb474f3</td>
    </tr>
    <tr>
      <th>Definition</th>
      <td>The status (available, unavailable) of two-dimensional photos of a subject/donor/specimen.</td>
    </tr>
    <tr>
      <th>Aliases</th>
      <td>photo_2d_available</td>
    </tr>
    <tr>
      <th>Data Type</th>
      <td>exclusive_categorical</td>
    </tr>
</tbody></table>
<br>

### Scan 3D Available

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td>scan 3d available</td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td>658e8a80-e232-438f-8c1e-d5f38724dc55</td>
    </tr>
    <tr>
      <th>Definition</th>
      <td>The status (available, unavailable) of three-dimensional scans of a subject/donor/specimen.</td>
    </tr>
    <tr>
      <th>Aliases</th>
      <td>scan_3d_available</td>
    </tr>
    <tr>
      <th>Data Type</th>
      <td>exclusive_categorical</td>
    </tr>
</tbody></table>
<br>

### Antemortem MRI Available

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td>antemortem MRI available</td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td>43a04caa-4f28-47ac-8a9d-74c40f10776f</td>
    </tr>
    <tr>
      <th>Definition</th>
      <td>The status (available, unavailable) of antemortem MRI images of a subject/donor/specimen.</td>
    </tr>
    <tr>
      <th>Aliases</th>
      <td>antemortem_mri_available</td>
    </tr>
    <tr>
      <th>Data Type</th>
      <td>exclusive_categorical</td>
    </tr>
</tbody></table>
<br>

### Postmortem MRI Available

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td>postmortem MRI available</td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td>0badd072-0c25-48c6-9357-44d5b5bc0818</td>
    </tr>
    <tr>
      <th>Definition</th>
      <td>The status (available, unavailable) of postmortem MRI images of a subject/donor/specimen.</td>
    </tr>
    <tr>
      <th>Aliases</th>
      <td>postmortem_mri_available</td>
    </tr>
    <tr>
      <th>Data Type</th>
      <td>exclusive_categorical</td>
    </tr>
</tbody></table>
<br>

### Postmortem MRI Type

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td>postmortem MRI type</td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td>64a607a9-21e6-4c73-8f2e-2d67b0dc51c8</td>
    </tr>
    <tr>
      <th>Definition</th>
      <td>The type of postmortem MRI that is available (cadeveric, fresh ex vivo, fixed ex vivo).</td>
    </tr>
    <tr>
      <th>Aliases</th>
      <td>postmortem_mri_type</td>
    </tr>
    <tr>
      <th>Data Type</th>
      <td>exclusive_categorical</td>
    </tr>
</tbody></table>
<br>

### Non-Brain Tissue Available

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td>non-brain tissue available</td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td>3a064c96-a956-4cf3-8b77-056b8e392f99</td>
    </tr>
    <tr>
      <th>Definition</th>
      <td>The status (yes, no) of whether non-brain tissue from this organism is available.</td>
    </tr>
    <tr>
      <th>Aliases</th>
      <td>non_brain_tissue_available</td>
    </tr>
    <tr>
      <th>Data Type</th>
      <td>exclusive_categorical</td>
    </tr>
</tbody></table>
<br>

### Tissue Type

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td>tissue type</td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td>33ccbc85-ae35-44d6-8bc6-c2fb91116cf7</td>
    </tr>
    <tr>
      <th>Definition</th>
      <td>The type of tissue (non-brain) that is available from this organism. </td>
    </tr>
    <tr>
      <th>Aliases</th>
      <td>tissue_type</td>
    </tr>
    <tr>
      <th>Data Type</th>
      <td>exclusive_categorical</td>
    </tr>
</tbody></table>
<br>

### Tissue Type Details

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td>tissue type details</td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td>f551cf87-2c6e-4b92-888d-6310e6a500d8</td>
    </tr>
    <tr>
      <th>Definition</th>
      <td>The details of the non-brain tissue that is available from this organism. </td>
    </tr>
    <tr>
      <th>Aliases</th>
      <td>tissue_type_details</td>
    </tr>
    <tr>
      <th>Data Type</th>
      <td>text</td>
    </tr>
</tbody></table>
<br>

### Birth Weight (lbs)

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td>birth weight value (lbs)</td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td>69d9a60d-32d5-4c3a-a26a-802d8f030c8d</td>
    </tr>
    <tr>
      <th>Definition</th>
      <td>The weight (at birth) of the subject/donor in pounds.</td>
    </tr>
    <tr>
      <th>Aliases</th>
      <td>birth_weight_lbs</td>
    </tr>
    <tr>
      <th>Data Type</th>
      <td>numeric</td>
    </tr>
</tbody></table>
<br>

### Birth Weight (oz)

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td>birth weight value (oz)</td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td>b6f30050-f762-4427-8533-31738e737ea2</td>
    </tr>
    <tr>
      <th>Definition</th>
      <td>The weight (at birth) of the subject/donor in ounces.</td>
    </tr>
    <tr>
      <th>Aliases</th>
      <td>birth_weight_oz</td>
    </tr>
    <tr>
      <th>Data Type</th>
      <td>numeric</td>
    </tr>
</tbody></table>
<br>

### Gestational Age Value (Weeks)

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td>gestational age value (weeks)</td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td>6d8a9b3f-792c-48c2-bd3c-56e52bb51672</td>
    </tr>
    <tr>
      <th>Definition</th>
      <td>The gestational age of the subject/donor in weeks.</td>
    </tr>
    <tr>
      <th>Aliases</th>
      <td>gestational_age_value_weeks</td>
    </tr>
    <tr>
      <th>Data Type</th>
      <td>numeric</td>
    </tr>
</tbody></table>
<br>

### Gestational Age Value (Days)

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td>gestational age value (days)</td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td>4e532e52-6e4c-46cd-9fde-96f97ef3b034</td>
    </tr>
    <tr>
      <th>Definition</th>
      <td>The gestational age of the subject/donor in days.</td>
    </tr>
    <tr>
      <th>Aliases</th>
      <td>gestational_age_value_days</td>
    </tr>
    <tr>
      <th>Data Type</th>
      <td>numeric</td>
    </tr>
</tbody></table>
<br>

### Species

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td>species</td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td>d11fb2ce-bfdb-4735-9b17-b6ba606520b1</td>
    </tr>
    <tr>
      <th>Definition</th>
      <td>The species of a subject/donor/sample/specimen.</td>
    </tr>
    <tr>
      <th>Aliases</th>
      <td>species</td>
    </tr>
    <tr>
      <th>Data Type</th>
      <td>exclusive_categorical</td>
    </tr>
</tbody></table>
<br>

### Social Group

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td>social group</td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td>7759b09d-a685-49fe-b7d8-e7f2b4772f52</td>
    </tr>
    <tr>
      <th>Definition</th>
      <td>The social group to which the subject belongs.</td>
    </tr>
    <tr>
      <th>Aliases</th>
      <td>social_group</td>
    </tr>
    <tr>
      <th>Data Type</th>
      <td>exclusive_categorical</td>
    </tr>
</tbody></table>
<br>

### Body Weight

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td>body weight</td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td>f2673501-b48f-4703-bb7e-d642b73c2ad4</td>
    </tr>
    <tr>
      <th>Definition</th>
      <td>The weight of the whole organism/donor/subject.</td>
    </tr>
    <tr>
      <th>Aliases</th>
      <td>body_weight</td>
    </tr>
    <tr>
      <th>Data Type</th>
      <td>numeric</td>
    </tr>
</tbody></table>
<br>

### Perfusion

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td>premortem perfusion done</td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td>1fc487d8-2403-4d7c-952f-7e502d5f8359</td>
    </tr>
    <tr>
      <th>Definition</th>
      <td>The status of premortem perfusion (done, not done).</td>
    </tr>
    <tr>
      <th>Aliases</th>
      <td>perfusion</td>
    </tr>
    <tr>
      <th>Data Type</th>
      <td>exclusive_categorical</td>
    </tr>
</tbody></table>
<br>

### Perfusate Type

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td>premortem perfusion buffer type</td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td>78d62e29-4323-4927-aec8-6fc8dc59a889</td>
    </tr>
    <tr>
      <th>Definition</th>
      <td>The type of premortem perfusion buffer that was used for premortem perfusion. </td>
    </tr>
    <tr>
      <th>Aliases</th>
      <td>perfusate_type</td>
    </tr>
    <tr>
      <th>Data Type</th>
      <td>text</td>
    </tr>
</tbody></table>
<br>

### Head off Time

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td>head off time</td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td>00ab5986-a8c4-4a7f-bf2b-6b5f08a97b25</td>
    </tr>
    <tr>
      <th>Definition</th>
      <td>The time at which the head was removed from the organism/donor/subject.</td>
    </tr>
    <tr>
      <th>Aliases</th>
      <td>head_off_time</td>
    </tr>
    <tr>
      <th>Data Type</th>
      <td>time</td>
    </tr>
</tbody></table>
<br>

### Brain Extraction Time

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td>brain extraction time</td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td>06be5810-7b9c-452e-b7ca-13eeb15179ca</td>
    </tr>
    <tr>
      <th>Definition</th>
      <td>The time at which the brain was extracted from the organism/donor/subject.</td>
    </tr>
    <tr>
      <th>Aliases</th>
      <td>brain_extraction_time</td>
    </tr>
    <tr>
      <th>Data Type</th>
      <td>time</td>
    </tr>
</tbody></table>
<br>

### Brain Fixed Time

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td>brain fixed time</td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td>2a09ecb4-0096-4a6c-b4f0-9b68cb231413</td>
    </tr>
    <tr>
      <th>Definition</th>
      <td>The time at which the brain specimen was fixed.</td>
    </tr>
    <tr>
      <th>Aliases</th>
      <td>brain_fixed_time</td>
    </tr>
    <tr>
      <th>Data Type</th>
      <td>time</td>
    </tr>
</tbody></table>
<br>

### Brain Frozen Time

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td>brain frozen time</td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td>fb01ce0d-1417-404a-978d-aad708c0404f</td>
    </tr>
    <tr>
      <th>Definition</th>
      <td>The time at which the brain specimen was frozen.</td>
    </tr>
    <tr>
      <th>Aliases</th>
      <td>brain_frozen_time</td>
    </tr>
    <tr>
      <th>Data Type</th>
      <td>time</td>
    </tr>
</tbody></table>
<br>

### Brain Fixation Method

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td>brain fixation method</td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td>8e0a01a9-ab7a-49a5-bf44-cc0af47719b1</td>
    </tr>
    <tr>
      <th>Definition</th>
      <td>The method used for fixing the brain specimen.</td>
    </tr>
    <tr>
      <th>Aliases</th>
      <td>brain_fixation_method</td>
    </tr>
    <tr>
      <th>Data Type</th>
      <td>exclusive_categorical</td>
    </tr>
</tbody></table>
<br>

### Brain Freeze Method

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td>brain freeze method</td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td>71237def-9b50-481f-a01d-65dc99e3493f</td>
    </tr>
    <tr>
      <th>Definition</th>
      <td>The method used for freezing the brain specimen. </td>
    </tr>
    <tr>
      <th>Aliases</th>
      <td>brain_freeze_method</td>
    </tr>
    <tr>
      <th>Data Type</th>
      <td>exclusive_categorical</td>
    </tr>
</tbody></table>
<br>

### Sedation Start Time

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td>sedation start time</td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td>0ad6cca0-d4ce-4cd8-bbce-520bc01db061</td>
    </tr>
    <tr>
      <th>Definition</th>
      <td>The time at which sedation of the organism/donor/subject began.</td>
    </tr>
    <tr>
      <th>Aliases</th>
      <td>sedation_start_time</td>
    </tr>
    <tr>
      <th>Data Type</th>
      <td>time</td>
    </tr>
</tbody></table>
<br>

### Sedation Total Dose

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td>sedation total dose</td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td>3c895613-4526-4b87-8620-7b42eff94fee</td>
    </tr>
    <tr>
      <th>Definition</th>
      <td>The total dose of sedation used on the organism/donor/subject.</td>
    </tr>
    <tr>
      <th>Aliases</th>
      <td>sedation_total_dose</td>
    </tr>
    <tr>
      <th>Data Type</th>
      <td>numeric</td>
    </tr>
</tbody></table>
<br>

### Euthanasia Time

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td>euthanasia time</td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td>14c541ab-7db3-4438-9328-c5f3098f5ff7</td>
    </tr>
    <tr>
      <th>Definition</th>
      <td>The time at which euthanasia of the organism/donor/subject occurred.</td>
    </tr>
    <tr>
      <th>Aliases</th>
      <td>euthanasia_time</td>
    </tr>
    <tr>
      <th>Data Type</th>
      <td>time</td>
    </tr>
</tbody></table>
<br>

### Euthanasia Dose

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td>euthanasia dose</td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td>d87c6869-c0d1-46b3-bb32-95dc3e3d5ed4</td>
    </tr>
    <tr>
      <th>Definition</th>
      <td>The dose of compouds used to euthanize the organism/donor/subject.</td>
    </tr>
    <tr>
      <th>Aliases</th>
      <td>euthanasia_dose</td>
    </tr>
    <tr>
      <th>Data Type</th>
      <td>numeric</td>
    </tr>
</tbody></table>
<br>

### Perfusion Time Start

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td>perfusion time start</td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td>7f94f8ad-82b7-4827-9614-838555a1f046</td>
    </tr>
    <tr>
      <th>Definition</th>
      <td>The time at which perfusion began.</td>
    </tr>
    <tr>
      <th>Aliases</th>
      <td>perfusion_time_start</td>
    </tr>
    <tr>
      <th>Data Type</th>
      <td>time</td>
    </tr>
</tbody></table>
<br>

### Perfusion Time End

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td>perfusion time end</td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td>6c873444-8306-4b3f-9e5a-97f6d34c88b3</td>
    </tr>
    <tr>
      <th>Definition</th>
      <td>The time at which perfusion ended.</td>
    </tr>
    <tr>
      <th>Aliases</th>
      <td>perfusion_time_end</td>
    </tr>
    <tr>
      <th>Data Type</th>
      <td></td>
    </tr>
</tbody></table>
<br>

### Trapping Date

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td>trapping date</td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td>e2603f30-af26-4d24-b9e7-dcbd47e09914</td>
    </tr>
    <tr>
      <th>Definition</th>
      <td>The date on which the subject/specimen was trapped.</td>
    </tr>
    <tr>
      <th>Aliases</th>
      <td>trapping_date</td>
    </tr>
    <tr>
      <th>Data Type</th>
      <td>date</td>
    </tr>
</tbody></table>
<br>

### Trapping Time

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td>trapping time</td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td>cc2ec53a-cd90-4bf5-9c49-c99ebb81498f</td>
    </tr>
    <tr>
      <th>Definition</th>
      <td>The time at which the subject/specimen was trapped.</td>
    </tr>
    <tr>
      <th>Aliases</th>
      <td>trapping_time</td>
    </tr>
    <tr>
      <th>Data Type</th>
      <td>time</td>
    </tr>
</tbody></table>
<br>

### Matriline

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td>matriline</td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td>ae0447a3-0504-43a3-95d5-4248e53d3224</td>
    </tr>
    <tr>
      <th>Definition</th>
      <td>The relavant matriline and patriline information for a subject/donor/sample/specimen.</td>
    </tr>
    <tr>
      <th>Aliases</th>
      <td>matriline</td>
    </tr>
    <tr>
      <th>Data Type</th>
      <td></td>
    </tr>
</tbody></table>
<br>

### Behavioral Scoring Available

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td>behavioral scoring available</td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td>ea33881a-9813-4111-979b-135355e8141e</td>
    </tr>
    <tr>
      <th>Definition</th>
      <td>The status (available, unavailable) of the behavioral scoring results for a subject/donor/specimen.</td>
    </tr>
    <tr>
      <th>Aliases</th>
      <td>behavioral_scoring_available</td>
    </tr>
    <tr>
      <th>Data Type</th>
      <td>exclusive_categorical</td>
    </tr>
</tbody></table>
<br>

### Behavioral Scoring Type

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td>behavioral scoring type</td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td>0a7a1eeb-8682-4261-8221-82d587dde0fa</td>
    </tr>
    <tr>
      <th>Definition</th>
      <td>The type of behavioral scoring that is available for a subject/donor/specimen.</td>
    </tr>
    <tr>
      <th>Aliases</th>
      <td>behavioral_scoring_type</td>
    </tr>
    <tr>
      <th>Data Type</th>
      <td>exclusive_categorical</td>
    </tr>
</tbody></table>
<br>

### Ordinal Dominance Rank

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td>ordinal dominance rank</td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td>080685e2-756a-446e-8d9d-5585c9ddd998</td>
    </tr>
    <tr>
      <th>Definition</th>
      <td>The dominance rank of the organism/subject/donor (ordinal).</td>
    </tr>
    <tr>
      <th>Aliases</th>
      <td>ordinal_dominance_rank</td>
    </tr>
    <tr>
      <th>Data Type</th>
      <td></td>
    </tr>
</tbody></table>
<br>

### Brain Size Anterior-Posterior

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td>brain size anterior-posterior</td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td>0830564a-26ba-41eb-888a-33d0c39ead8f</td>
    </tr>
    <tr>
      <th>Definition</th>
      <td>The size of the brain specimen in the anterior-posterior axis.</td>
    </tr>
    <tr>
      <th>Aliases</th>
      <td>brain_size_anterior_posterior</td>
    </tr>
    <tr>
      <th>Data Type</th>
      <td>numeric</td>
    </tr>
</tbody></table>
<br>

### Brain Size Medial-Lateral

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td>brain size medial-lateral</td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td>4722f739-71f6-4001-9784-afef8f9f2d0e</td>
    </tr>
    <tr>
      <th>Definition</th>
      <td>The size of the brain specimen in the medial-lateral axis.</td>
    </tr>
    <tr>
      <th>Aliases</th>
      <td>brain_size_medial_lateral</td>
    </tr>
    <tr>
      <th>Data Type</th>
      <td>numeric</td>
    </tr>
</tbody></table>
<br>

### Brain Size Dorsal-Ventral

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td>brain size dorsal-ventral</td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td>e683f5ee-696f-4baf-a9bf-2f12226ceb4a</td>
    </tr>
    <tr>
      <th>Definition</th>
      <td>The size of the brain specimen in the dorsal-ventral axis.</td>
    </tr>
    <tr>
      <th>Aliases</th>
      <td>brain_size_dorsal_ventral</td>
    </tr>
    <tr>
      <th>Data Type</th>
      <td>numeric</td>
    </tr>
</tbody></table>
<br>

### Brain Size Unit Type

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td>brain size unit</td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td>4d0c44c6-e620-455d-989e-126c3c81ec91</td>
    </tr>
    <tr>
      <th>Definition</th>
      <td>The unit that the brain size measurements are recorded.</td>
    </tr>
    <tr>
      <th>Aliases</th>
      <td>brain_size_unit_type</td>
    </tr>
    <tr>
      <th>Data Type</th>
      <td>exclusive_categorical</td>
    </tr>
</tbody></table>
<br>

### Histological Stains Available

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td>histological stains available</td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td>4b868ba6-dba8-45e3-a43e-88e421625cab</td>
    </tr>
    <tr>
      <th>Definition</th>
      <td>The status (available, unavailable) of histological stainings of a specimen.</td>
    </tr>
    <tr>
      <th>Aliases</th>
      <td>histological_stains_available</td>
    </tr>
    <tr>
      <th>Data Type</th>
      <td>exclusive_categorical</td>
    </tr>
</tbody></table>
<br>

### Histological Stain Type

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td>histological stains type</td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td>6723e756-e4c1-42c7-bf2d-ee2e300b88ff</td>
    </tr>
    <tr>
      <th>Definition</th>
      <td>The type of histological stains available for a specimen.</td>
    </tr>
    <tr>
      <th>Aliases</th>
      <td>histological_stain_type</td>
    </tr>
    <tr>
      <th>Data Type</th>
      <td>exclusive_categorical</td>
    </tr>
</tbody></table>
<br>

## Whole Brain Spatial Omics

The data in whole brain spatial omics is the metadata essential for whole brain spatial omics experiments.

The following tables describe the whole brain spatial omics metadata. If an entry in the table is empty, the schema does not have any other requirements on data in those layers beyond the ones listed above.

Curators must annotate the following columns:

### Local Donor ID

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td>local donor ID</td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td>f8af20f7-e8b8-47b5-8a68-9ec1f913ffdf</td>
    </tr>
    <tr>
      <th>Definition</th>
      <td></td>
    </tr>
    <tr>
      <th>Aliases</th>
      <td>subject_id</td>
    </tr>
    <tr>
      <th>Data Type</th>
      <td>text</td>
    </tr>
</tbody></table>
<br>

### Repository

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td>repository</td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td>408682ed-0e27-41e2-b9fa-f05674366d6e</td>
    </tr>
    <tr>
      <th>Definition</th>
      <td>'Repository' trailing modifier (qualifier, 'repository') of 'xref' links of 'Format' concepts. When 'true', the link is pointing to the public source-code repository where the given data format is developed or maintained.</td>
    </tr>
    <tr>
      <th>Aliases</th>
      <td>repository</td>
    </tr>
    <tr>
      <th>Data Type</th>
      <td>inclusive_categorical</td>
    </tr>
</tbody></table>
<br>

### Donor Source

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td>donor source</td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td>0d0cf732-0f76-409d-9a73-7a96d829d3d3</td>
    </tr>
    <tr>
      <th>Definition</th>
      <td>The origin of the donor/subject in this experiment.</td>
    </tr>
    <tr>
      <th>Aliases</th>
      <td>donor_source</td>
    </tr>
    <tr>
      <th>Data Type</th>
      <td>inclusive_categorical</td>
    </tr>
</tbody></table>
<br>

### Sex at Birth

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td>sex at birth</td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td>c819b9d5-2fde-40b2-bf0d-e07b56f96ac9</td>
    </tr>
    <tr>
      <th>Definition</th>
      <td>An organismal quality inhering in a bearer by virtue of the bearer's ability to undergo sexual reproduction in order to differentiate the individuals or types involved.</td>
    </tr>
    <tr>
      <th>Aliases</th>
      <td>sex</td>
    </tr>
    <tr>
      <th>Data Type</th>
      <td>exclusive_categorical</td>
    </tr>
</tbody></table>
<br>

### Age Value (Years)

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td>age value (years)</td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td>14eb923a-161d-45e2-889d-81fea7b632b6</td>
    </tr>
    <tr>
      <th>Definition</th>
      <td>A time quality inhering in a bearer by virtue of how long the bearer has existed.</td>
    </tr>
    <tr>
      <th>Aliases</th>
      <td>age_of_death</td>
    </tr>
    <tr>
      <th>Data Type</th>
      <td>numeric</td>
    </tr>
</tbody></table>
<br>

### Year of Death

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td>year of death</td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td>60445046-d9d8-4f00-959e-9a4c42613e5e</td>
    </tr>
    <tr>
      <th>Definition</th>
      <td>The year wherein the subject or donor has ceased to exist.</td>
    </tr>
    <tr>
      <th>Aliases</th>
      <td>year_of_death</td>
    </tr>
    <tr>
      <th>Data Type</th>
      <td>date</td>
    </tr>
</tbody></table>
<br>

### Hemisphere

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td>hemisphere</td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td>68b7a28b-d695-4ec9-800b-6a27ca206081</td>
    </tr>
    <tr>
      <th>Definition</th>
      <td>One of two bilateral, largely symmetrical organ subdivisions within the telencephalon which contain the cerebral cortex and cerebral white matter.</td>
    </tr>
    <tr>
      <th>Aliases</th>
      <td>hemisphere</td>
    </tr>
    <tr>
      <th>Data Type</th>
      <td>exclusive_categorical</td>
    </tr>
</tbody></table>
<br>

### Post Mortem Interval

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td>post mortem interval</td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td>6fd5c5ac-b128-4a4a-ae98-09eaeba22f92</td>
    </tr>
    <tr>
      <th>Definition</th>
      <td>The length of the temporal interval between the time of death of the subject/donor and the time at which the specimen is made.</td>
    </tr>
    <tr>
      <th>Aliases</th>
      <td>post_mortem_interval</td>
    </tr>
    <tr>
      <th>Data Type</th>
      <td>numeric</td>
    </tr>
</tbody></table>
<br>

### RIN

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td>RIN</td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td>cd472c0d-0b64-45c9-a38e-e54d15cea953</td>
    </tr>
    <tr>
      <th>Definition</th>
      <td>The RNA integrity number value of a specimen.</td>
    </tr>
    <tr>
      <th>Aliases</th>
      <td>rin</td>
    </tr>
    <tr>
      <th>Data Type</th>
      <td>numeric</td>
    </tr>
</tbody></table>
<br>

### RIN Tissue Source

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td>RIN tissue source</td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td>d547ee51-9ec3-489c-8e49-7d8cd94080a8</td>
    </tr>
    <tr>
      <th>Definition</th>
      <td>The tissue sample location or identifier that is used for calculating the RNA integrity number.</td>
    </tr>
    <tr>
      <th>Aliases</th>
      <td>rin_tissue_source</td>
    </tr>
    <tr>
      <th>Data Type</th>
      <td>text</td>
    </tr>
</tbody></table>
<br>

### Brain Weight

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td>brain weight measurement</td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td>546fc32d-f8a2-4c00-924a-8c4730f11f51</td>
    </tr>
    <tr>
      <th>Definition</th>
      <td>The weight of a brain specimen.</td>
    </tr>
    <tr>
      <th>Aliases</th>
      <td>brain_weight</td>
    </tr>
    <tr>
      <th>Data Type</th>
      <td>numeric</td>
    </tr>
</tbody></table>
<br>

### Photo 2D Available

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td>photo 2d available</td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td>611beda8-1ac6-4183-a284-04a30bb474f3</td>
    </tr>
    <tr>
      <th>Definition</th>
      <td>The status (available, unavailable) of two-dimensional photos of a subject/donor/specimen.</td>
    </tr>
    <tr>
      <th>Aliases</th>
      <td>photo_2d_available</td>
    </tr>
    <tr>
      <th>Data Type</th>
      <td>exclusive_categorical</td>
    </tr>
</tbody></table>
<br>

### Scan 3D Available

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td>scan 3d available</td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td>658e8a80-e232-438f-8c1e-d5f38724dc55</td>
    </tr>
    <tr>
      <th>Definition</th>
      <td>The status (available, unavailable) of three-dimensional scans of a subject/donor/specimen.</td>
    </tr>
    <tr>
      <th>Aliases</th>
      <td>scan_3d_available</td>
    </tr>
    <tr>
      <th>Data Type</th>
      <td>exclusive_categorical</td>
    </tr>
</tbody></table>
<br>

### Antemortem MRI Available

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td>antemortem MRI available</td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td>43a04caa-4f28-47ac-8a9d-74c40f10776f</td>
    </tr>
    <tr>
      <th>Definition</th>
      <td>The status (available, unavailable) of antemortem MRI images of a subject/donor/specimen.</td>
    </tr>
    <tr>
      <th>Aliases</th>
      <td>antemortem_mri_available</td>
    </tr>
    <tr>
      <th>Data Type</th>
      <td>exclusive_categorical</td>
    </tr>
</tbody></table>
<br>

## Appendix

<!-- schema-properties-start:wb-omics-spatial -->
## WB Omics Spatial properties
*Auto-generated from CSV. Do not edit this section manually.*

**Status:** Accepted by MOWG &middot; **Version:** 1.0.0 &middot; **Date:** 2024-07-08

### Properties

#### General Specimen Data

| Property | Type | Required | Aliases | Description |
|----------|------|----------|---------|-------------|
| [`hemisphere`](#hemisphere) | exclusive_categorical | yes | hemisphere | One of two bilateral, largely symmetrical organ subdivisions within the telencephalon which contain the cerebral cortex … |
| [`post mortem interval`](#post-mortem-interval) | numeric | yes | post_mortem_interval | The length of the temporal interval between the time of death of the subject/donor and the time at which the specimen is… |
| [`RIN`](#rin) | numeric | yes | rin | The RNA integrity number value of a specimen. |
| [`RIN tissue source`](#rin-tissue-source) | text | yes | rin_tissue_source | The tissue sample location or identifier that is used for calculating the RNA integrity number. |
| [`brain weight measurement`](#brain-weight-measurement) | numeric | yes | brain_weight | The weight of a brain specimen. |
| [`photo 2d available`](#photo-2d-available) | exclusive_categorical | yes | photo_2d_available | The status (available, unavailable) of two-dimensional photos of a subject/donor/specimen. |
| [`scan 3d available`](#scan-3d-available) | exclusive_categorical | yes | scan_3d_available | The status (available, unavailable) of three-dimensional scans of a subject/donor/specimen. |
| [`antemortem MRI available`](#antemortem-mri-available) | exclusive_categorical | yes | antemortem_mri_available | The status (available, unavailable) of antemortem MRI images of a subject/donor/specimen. |

#### General Subject Fields

| Property | Type | Required | Aliases | Description |
|----------|------|----------|---------|-------------|
| [`local donor ID`](#local-donor-id) | text | yes | subject_id | An identifier that uniquely denotes objects only within the scope of a specific object aggregate and that is not registe… |
| [`repository`](#repository) | inclusive_categorical | yes | repository | &#x27;Repository&#x27; trailing modifier (qualifier, &#x27;repository&#x27;) of &#x27;xref&#x27; links of &#x27;Format&#x27; concepts. When &#x27;true&#x27;, the link is … |
| [`donor source`](#donor-source) | inclusive_categorical | yes | donor_source | The origin of the donor/subject in this experiment. |
| [`sex at birth`](#sex-at-birth) | exclusive_categorical | yes | sex | An organismal quality inhering in a bearer by virtue of the bearer&#x27;s ability to undergo sexual reproduction in order to … |
| [`age value (years)`](#age-value-(years)) | numeric | yes | age_of_death | A time quality inhering in a bearer by virtue of how long the bearer has existed. [PATO] |
| [`year of death`](#year-of-death) | date | yes | year_of_death | The year wherein the subject or donor has ceased to exist. |

### Property Details

#### General Specimen Data

<div id="hemisphere" class="field-detail">
<h5><code>hemisphere</code> <em>(required)</em></h5>
<ul>
<li><strong>BICAN UUID:</strong> <code>68b7a28b-d695-4ec9-800b-6a27ca206081</code></li>
<li><strong>Data Type:</strong> <code>exclusive_categorical</code></li>
<li><strong>Aliases:</strong> hemisphere</li>
</ul>
<p>One of two bilateral, largely symmetrical organ subdivisions within the telencephalon which contain the cerebral cortex and cerebral white matter. [UBERON]</p>
</div>

<div id="post-mortem-interval" class="field-detail">
<h5><code>post mortem interval</code> <em>(required)</em></h5>
<ul>
<li><strong>BICAN UUID:</strong> <code>6fd5c5ac-b128-4a4a-ae98-09eaeba22f92</code></li>
<li><strong>Data Type:</strong> <code>numeric</code></li>
<li><strong>Aliases:</strong> post_mortem_interval</li>
</ul>
<p>The length of the temporal interval between the time of death of the subject/donor and the time at which the specimen is made.</p>
</div>

<div id="rin" class="field-detail">
<h5><code>RIN</code> <em>(required)</em></h5>
<ul>
<li><strong>BICAN UUID:</strong> <code>cd472c0d-0b64-45c9-a38e-e54d15cea953</code></li>
<li><strong>Data Type:</strong> <code>numeric</code></li>
<li><strong>Aliases:</strong> rin</li>
</ul>
<p>The RNA integrity number value of a specimen.</p>
</div>

<div id="rin-tissue-source" class="field-detail">
<h5><code>RIN tissue source</code> <em>(required)</em></h5>
<ul>
<li><strong>BICAN UUID:</strong> <code>d547ee51-9ec3-489c-8e49-7d8cd94080a8</code></li>
<li><strong>Data Type:</strong> <code>text</code></li>
<li><strong>Aliases:</strong> rin_tissue_source</li>
</ul>
<p>The tissue sample location or identifier that is used for calculating the RNA integrity number.</p>
</div>

<div id="brain-weight-measurement" class="field-detail">
<h5><code>brain weight measurement</code> <em>(required)</em></h5>
<ul>
<li><strong>BICAN UUID:</strong> <code>546fc32d-f8a2-4c00-924a-8c4730f11f51</code></li>
<li><strong>Data Type:</strong> <code>numeric</code></li>
<li><strong>Aliases:</strong> brain_weight</li>
</ul>
<p>The weight of a brain specimen.</p>
</div>

<div id="photo-2d-available" class="field-detail">
<h5><code>photo 2d available</code> <em>(required)</em></h5>
<ul>
<li><strong>BICAN UUID:</strong> <code>611beda8-1ac6-4183-a284-04a30bb474f3</code></li>
<li><strong>Data Type:</strong> <code>exclusive_categorical</code></li>
<li><strong>Aliases:</strong> photo_2d_available</li>
</ul>
<p>The status (available, unavailable) of two-dimensional photos of a subject/donor/specimen.</p>
</div>

<div id="scan-3d-available" class="field-detail">
<h5><code>scan 3d available</code> <em>(required)</em></h5>
<ul>
<li><strong>BICAN UUID:</strong> <code>658e8a80-e232-438f-8c1e-d5f38724dc55</code></li>
<li><strong>Data Type:</strong> <code>exclusive_categorical</code></li>
<li><strong>Aliases:</strong> scan_3d_available</li>
</ul>
<p>The status (available, unavailable) of three-dimensional scans of a subject/donor/specimen.</p>
</div>

<div id="antemortem-mri-available" class="field-detail">
<h5><code>antemortem MRI available</code> <em>(required)</em></h5>
<ul>
<li><strong>BICAN UUID:</strong> <code>43a04caa-4f28-47ac-8a9d-74c40f10776f</code></li>
<li><strong>Data Type:</strong> <code>exclusive_categorical</code></li>
<li><strong>Aliases:</strong> antemortem_mri_available</li>
</ul>
<p>The status (available, unavailable) of antemortem MRI images of a subject/donor/specimen.</p>
</div>

#### General Subject Fields

<div id="local-donor-id" class="field-detail">
<h5><code>local donor ID</code> <em>(required)</em></h5>
<ul>
<li><strong>BICAN UUID:</strong> <code>f8af20f7-e8b8-47b5-8a68-9ec1f913ffdf</code></li>
<li><strong>Data Type:</strong> <code>text</code></li>
<li><strong>Aliases:</strong> subject_id</li>
</ul>
<p>An identifier that uniquely denotes objects only within the scope of a specific object aggregate and that is not registered in an identifier registry. [Allotrope]</p>
</div>

<div id="repository" class="field-detail">
<h5><code>repository</code> <em>(required)</em></h5>
<ul>
<li><strong>BICAN UUID:</strong> <code>408682ed-0e27-41e2-b9fa-f05674366d6e</code></li>
<li><strong>Data Type:</strong> <code>inclusive_categorical</code></li>
<li><strong>Aliases:</strong> repository</li>
</ul>
<p>&#x27;Repository&#x27; trailing modifier (qualifier, &#x27;repository&#x27;) of &#x27;xref&#x27; links of &#x27;Format&#x27; concepts. When &#x27;true&#x27;, the link is pointing to the public source-code repository where the given data format is developed or maintained. [EDAM]</p>
</div>

<div id="donor-source" class="field-detail">
<h5><code>donor source</code> <em>(required)</em></h5>
<ul>
<li><strong>BICAN UUID:</strong> <code>0d0cf732-0f76-409d-9a73-7a96d829d3d3</code></li>
<li><strong>Data Type:</strong> <code>inclusive_categorical</code></li>
<li><strong>Aliases:</strong> donor_source</li>
</ul>
<p>The origin of the donor/subject in this experiment.</p>
</div>

<div id="sex-at-birth" class="field-detail">
<h5><code>sex at birth</code> <em>(required)</em></h5>
<ul>
<li><strong>BICAN UUID:</strong> <code>c819b9d5-2fde-40b2-bf0d-e07b56f96ac9</code></li>
<li><strong>Data Type:</strong> <code>exclusive_categorical</code></li>
<li><strong>Aliases:</strong> sex</li>
</ul>
<p>An organismal quality inhering in a bearer by virtue of the bearer&#x27;s ability to undergo sexual reproduction in order to differentiate the individuals or types involved. [PATO]</p>
</div>

<div id="age-value-(years)" class="field-detail">
<h5><code>age value (years)</code> <em>(required)</em></h5>
<ul>
<li><strong>BICAN UUID:</strong> <code>14eb923a-161d-45e2-889d-81fea7b632b6</code></li>
<li><strong>Data Type:</strong> <code>numeric</code></li>
<li><strong>Aliases:</strong> age_of_death</li>
</ul>
<p>A time quality inhering in a bearer by virtue of how long the bearer has existed. [PATO]</p>
</div>

<div id="year-of-death" class="field-detail">
<h5><code>year of death</code> <em>(required)</em></h5>
<ul>
<li><strong>BICAN UUID:</strong> <code>60445046-d9d8-4f00-959e-9a4c42613e5e</code></li>
<li><strong>Data Type:</strong> <code>date</code></li>
<li><strong>Aliases:</strong> year_of_death</li>
</ul>
<p>The year wherein the subject or donor has ceased to exist.</p>
</div>

<!-- schema-properties-end:wb-omics-spatial -->

<!-- schema-properties-start:population -->
## Population properties
*Auto-generated from CSV. Do not edit this section manually.*

**Status:** Accepted by MOWG &middot; **Version:** 1.0.0 &middot; **Date:** 2024-07-08

### Properties

| Property | Type | Required | Aliases | Description |
|----------|------|----------|---------|-------------|
| [`trapping date`](#trapping-date) | date | yes | trapping_date | The date on which the subject/specimen was trapped. |
| [`trapping time`](#trapping-time) | time | yes | trapping_time | The time at which the subject/specimen was trapped. |

#### Behavioral Measurements

| Property | Type | Required | Aliases | Description |
|----------|------|----------|---------|-------------|
| [`behavioral scoring available`](#behavioral-scoring-available) | exclusive_categorical | yes | behavioral_scoring_available | The status (available, unavailable) of the behavioral scoring results for a subject/donor/specimen. |
| [`behavioral scoring type`](#behavioral-scoring-type) | exclusive_categorical | no | behavioral_scoring_type | The type of behavioral scoring that is available for a subject/donor/specimen. |
| [`ordinal dominance rank`](#ordinal-dominance-rank) | numeric | yes | ordinal_dominance_rank |  |

#### Family History

| Property | Type | Required | Aliases | Description |
|----------|------|----------|---------|-------------|
| [`matriline`](#matriline) | — | yes | matriline | The relavant matriline and patriline information for a subject/donor/sample/specimen. |

#### General Specimen Data

| Property | Type | Required | Aliases | Description |
|----------|------|----------|---------|-------------|
| [`hemisphere`](#hemisphere) | exclusive_categorical | yes | hemisphere | One of two bilateral, largely symmetrical organ subdivisions within the telencephalon which contain the cerebral cortex … |
| [`post mortem interval`](#post-mortem-interval) | numeric | yes | post_mortem_interval | The length of the temporal interval between the time of death of the subject/donor and the time at which the specimen is… |
| [`left hemisphere preparation`](#left-hemisphere-preparation) | exclusive_categorical | yes | left_hemisphere_preparation | The type of preparation method used for the left hemisphere. |
| [`left hemisphere preparation specify`](#left-hemisphere-preparation-specify) | text | yes | left_hemisphere_preparation_specify | Specific details about the type of preparation method used for the left hemisphere. |
| [`right hemisphere preparation`](#right-hemisphere-preparation) | exclusive_categorical | yes | right_hemisphere_preparation | The type of preparation method used for the right hemisphere. |
| [`right hemisphere preparation specify`](#right-hemisphere-preparation-specify) | text | yes | right_hemisphere_preparation_specify | Specific details about the type of preparation method used for the right hemisphere. |
| [`RIN`](#rin) | numeric | yes | rin | The RNA integrity number value of a specimen. |
| [`RIN tissue source`](#rin-tissue-source) | text | yes | rin_tissue_source | The tissue sample location or identifier that is used for calculating the RNA integrity number. |
| [`RIN testing organization`](#rin-testing-organization) | text | yes | rin_testing_organization | The organization that determines the RNA integrity number of a sample/specimen. |
| [`RINe`](#rine) | numeric | yes | rine | A type of RIN (RNA integrity number) value that represents the relative ratio of the signal in the fast zone to the 18S … |
| [`RINe tissue source`](#rine-tissue-source) | text | yes | rine_tissue_source | The tissue sample location or identifier that is used for calculating the RINe number. |
| [`RINe testing organization`](#rine-testing-organization) | text | yes | rine_testing_organization | The organization that determines the RINe number. |
| [`pH`](#ph) | numeric | yes | ph | The value of a measurement of acidity or basicity of a tissue, sample, or specimen. |
| [`brain weight measurement`](#brain-weight-measurement) | numeric | yes | brain_weight | The weight of a brain specimen. |
| [`brain tissue weighed type`](#brain-tissue-weighed-type) | exclusive_categorical | yes | weighed_type | The state of a brain specimen when it is weighed (fresh, frozen, fixed). |
| [`photo 2d available`](#photo-2d-available) | exclusive_categorical | yes | photo_2d_available | The status (available, unavailable) of two-dimensional photos of a subject/donor/specimen. |
| [`scan 3d available`](#scan-3d-available) | exclusive_categorical | yes | scan_3d_available | The status (available, unavailable) of three-dimensional scans of a subject/donor/specimen. |
| [`antemortem MRI available`](#antemortem-mri-available) | exclusive_categorical | yes | antemortem_mri_available | The status (available, unavailable) of antemortem MRI images of a subject/donor/specimen. |
| [`postmortem MRI available`](#postmortem-mri-available) | exclusive_categorical | yes | postmortem_mri_available | The status (available, unavailable) of postmortem MRI images of a subject/donor/specimen. |
| [`postmortem MRI type`](#postmortem-mri-type) | exclusive_categorical | no | postmortem_mri_type | The type of postmortem MRI that is available (cadeveric, fresh ex vivo, fixed ex vivo). |
| [`premortem perfusion done`](#premortem-perfusion-done) | exclusive_categorical | yes | perfusion | The status of premortem perfusion (done, not done). |
| [`premortem perfusion buffer type`](#premortem-perfusion-buffer-type) | text | no | perfusate_type | The type of premortem perfusion buffer that was used for premortem perfusion. |
| [`head off time`](#head-off-time) | time | yes | head_off_time | The time at which the head was removed from the organism/donor/subject. |
| [`brain extraction time`](#brain-extraction-time) | time | yes | brain_extraction_time | The time at which the brain was extracted from the organism/donor/subject. |
| [`brain fixed time`](#brain-fixed-time) | time | no | brain_fixed_time | The time at which the brain specimen was fixed. |
| [`brain frozen time`](#brain-frozen-time) | time | no | brain_frozen_time | The time at which the brain specimen was frozen. |
| [`brain fixation method`](#brain-fixation-method) | exclusive_categorical | no | brain_fixation_method | The method used for fixing the brain specimen. |
| [`brain freeze method`](#brain-freeze-method) | exclusive_categorical | no | brain_freeze_method | The method used for freezing the brain specimen. |
| [`sedation start time`](#sedation-start-time) | time | yes | sedation_start_time | The time at which sedation of the organism/donor/subject began. |
| [`sedation total dose`](#sedation-total-dose) | numeric | yes | sedation_total_dose | The total dose of sedation used on the organism/donor/subject. |
| [`euthanasia time`](#euthanasia-time) | time | yes | euthanasia_time | The time at which euthanasia of the organism/donor/subject occurred. |
| [`euthanasia dose`](#euthanasia-dose) | numeric | yes | euthanasia_dose | The dose of compouds used to euthanize the organism/donor/subject. |
| [`perfusion time start`](#perfusion-time-start) | time | yes | perfusion_time_start | The time at which perfusion began. |
| [`perfusion time end`](#perfusion-time-end) | time | yes | perfusion_time_end | The time at which perfusion ended. |
| [`brain size anterior-posterior`](#brain-size-anterior-posterior) | numeric | yes | brain_size_anterior_posterior | The size of the brain specimen in the anterior-posterior axis. |
| [`brain size medial-lateral`](#brain-size-medial-lateral) | numeric | yes | brain_size_medial_lateral | The size of the brain specimen in the medial-lateral axis. |
| [`brain size dorsal-ventral`](#brain-size-dorsal-ventral) | numeric | yes | brain_size_dorsal_ventral | The size of the brain specimen in the dorsal-ventral axis. |
| [`brain size unit`](#brain-size-unit) | exclusive_categorical | yes | brain_size_unit_type | The unit that the brain size measurements are recorded. |
| [`histological stains available`](#histological-stains-available) | exclusive_categorical | yes | histological_stains_available | The status (available, unavailable) of histological stainings of a specimen. |
| [`histological stains type`](#histological-stains-type) | exclusive_categorical | no | histological_stain_type | The type of histological stains available for a specimen. |

#### General Subject Fields

| Property | Type | Required | Aliases | Description |
|----------|------|----------|---------|-------------|
| [`local donor ID`](#local-donor-id) | text | yes | subject_id | An identifier that uniquely denotes objects only within the scope of a specific object aggregate and that is not registe… |
| [`repository`](#repository) | inclusive_categorical | yes | repository | &#x27;Repository&#x27; trailing modifier (qualifier, &#x27;repository&#x27;) of &#x27;xref&#x27; links of &#x27;Format&#x27; concepts. When &#x27;true&#x27;, the link is … |
| [`donor source`](#donor-source) | inclusive_categorical | yes | donor_source | The origin of the donor/subject in this experiment. |
| [`sex at birth`](#sex-at-birth) | exclusive_categorical | yes | sex | An organismal quality inhering in a bearer by virtue of the bearer&#x27;s ability to undergo sexual reproduction in order to … |
| [`age value (years)`](#age-value-(years)) | numeric | yes | age_of_death | A time quality inhering in a bearer by virtue of how long the bearer has existed. [PATO] |
| [`year of death`](#year-of-death) | date | yes | year_of_death | The year wherein the subject or donor has ceased to exist. |
| [`autopsy report`](#autopsy-report) | exclusive_categorical | yes | autopsy_report | A document assembled by an author for the purpose of providing information regarding the cause of death of a subject for… |
| [`cause of death`](#cause-of-death) | text | yes | cause_of_death | The circumstance or condition that results in the death of a living being. [NCIT] |
| [`cause of death code`](#cause-of-death-code) | text | yes | cause_of_death_code | The ISO code that denotes the circumstance or condition that results in the death of a living being. [NCIT] |
| [`manner of death`](#manner-of-death) | exclusive_categorical | yes | manner_of_death | The manner of death is the determination of how the injury or disease leads to death.  There are five manners of death (… |
| [`medical records reviewed`](#medical-records-reviewed) | exclusive_categorical | yes | medical_records_reviewed | The status (reviewed, not reviewed) of the medical records of the subject/donor. |
| [`species`](#species) | exclusive_categorical | yes | species | The species of a subject/donor/sample/specimen. |
| [`social group`](#social-group) | exclusive_categorical | yes | social_group | The social group to which the subject belongs. |
| [`body weight`](#body-weight) | numeric | yes | body_weight | The weight of the whole organism/donor/subject. |

#### Infant Medical History

| Property | Type | Required | Aliases | Description |
|----------|------|----------|---------|-------------|
| [`birth weight value (lbs)`](#birth-weight-value-(lbs)) | numeric | yes | birth_weight_lbs | The weight (at birth) of the subject/donor in pounds. |
| [`birth weight value (oz)`](#birth-weight-value-(oz)) | numeric | yes | birth_weight_oz | The weight (at birth) of the subject/donor in ounces. |
| [`gestational age value (weeks)`](#gestational-age-value-(weeks)) | numeric | yes | gestational_age_value_weeks | The gestational age of the subject/donor in weeks. |
| [`gestational age value (days)`](#gestational-age-value-(days)) | numeric | yes | gestational_age_value_days | The gestational age of the subject/donor in days. |

#### Non-Brain Specimen Collected

| Property | Type | Required | Aliases | Description |
|----------|------|----------|---------|-------------|
| [`non-brain tissue available`](#non-brain-tissue-available) | exclusive_categorical | yes | non_brain_tissue_available | The status (yes, no) of whether non-brain tissue from this organism is available. |
| [`tissue type`](#tissue-type) | exclusive_categorical | yes | tissue_type | The type of tissue (non-brain) that is available from this organism. |
| [`tissue type details`](#tissue-type-details) | text | no | tissue_type_details | The details of the non-brain tissue that is available from this organism. |

### Property Details

<div id="trapping-date" class="field-detail">
<h5><code>trapping date</code> <em>(required)</em></h5>
<ul>
<li><strong>BICAN UUID:</strong> <code>e2603f30-af26-4d24-b9e7-dcbd47e09914</code></li>
<li><strong>Data Type:</strong> <code>date</code></li>
<li><strong>Aliases:</strong> trapping_date</li>
</ul>
<p>The date on which the subject/specimen was trapped.</p>
</div>

<div id="trapping-time" class="field-detail">
<h5><code>trapping time</code> <em>(required)</em></h5>
<ul>
<li><strong>BICAN UUID:</strong> <code>cc2ec53a-cd90-4bf5-9c49-c99ebb81498f</code></li>
<li><strong>Data Type:</strong> <code>time</code></li>
<li><strong>Aliases:</strong> trapping_time</li>
</ul>
<p>The time at which the subject/specimen was trapped.</p>
</div>

#### Behavioral Measurements

<div id="behavioral-scoring-available" class="field-detail">
<h5><code>behavioral scoring available</code> <em>(required)</em></h5>
<ul>
<li><strong>BICAN UUID:</strong> <code>ea33881a-9813-4111-979b-135355e8141e</code></li>
<li><strong>Data Type:</strong> <code>exclusive_categorical</code></li>
<li><strong>Aliases:</strong> behavioral_scoring_available</li>
</ul>
<p>The status (available, unavailable) of the behavioral scoring results for a subject/donor/specimen.</p>
</div>

<div id="behavioral-scoring-type" class="field-detail">
<h5><code>behavioral scoring type</code> <em>(optional)</em></h5>
<ul>
<li><strong>BICAN UUID:</strong> <code>0a7a1eeb-8682-4261-8221-82d587dde0fa</code></li>
<li><strong>Data Type:</strong> <code>exclusive_categorical</code></li>
<li><strong>Aliases:</strong> behavioral_scoring_type</li>
</ul>
<p>The type of behavioral scoring that is available for a subject/donor/specimen.</p>
</div>

<div id="ordinal-dominance-rank" class="field-detail">
<h5><code>ordinal dominance rank</code> <em>(required)</em></h5>
<ul>
<li><strong>BICAN UUID:</strong> <code>080685e2-756a-446e-8d9d-5585c9ddd998</code></li>
<li><strong>Data Type:</strong> <code>numeric</code></li>
<li><strong>Aliases:</strong> ordinal_dominance_rank</li>
</ul>
<p></p>
</div>

#### Family History

<div id="matriline" class="field-detail">
<h5><code>matriline</code> <em>(required)</em></h5>
<ul>
<li><strong>BICAN UUID:</strong> <code>ae0447a3-0504-43a3-95d5-4248e53d3224</code></li>
<li><strong>Aliases:</strong> matriline</li>
</ul>
<p>The relavant matriline and patriline information for a subject/donor/sample/specimen.</p>
</div>

#### General Specimen Data

<div id="hemisphere" class="field-detail">
<h5><code>hemisphere</code> <em>(required)</em></h5>
<ul>
<li><strong>BICAN UUID:</strong> <code>68b7a28b-d695-4ec9-800b-6a27ca206081</code></li>
<li><strong>Data Type:</strong> <code>exclusive_categorical</code></li>
<li><strong>Aliases:</strong> hemisphere</li>
</ul>
<p>One of two bilateral, largely symmetrical organ subdivisions within the telencephalon which contain the cerebral cortex and cerebral white matter. [UBERON]</p>
</div>

<div id="post-mortem-interval" class="field-detail">
<h5><code>post mortem interval</code> <em>(required)</em></h5>
<ul>
<li><strong>BICAN UUID:</strong> <code>6fd5c5ac-b128-4a4a-ae98-09eaeba22f92</code></li>
<li><strong>Data Type:</strong> <code>numeric</code></li>
<li><strong>Aliases:</strong> post_mortem_interval</li>
</ul>
<p>The length of the temporal interval between the time of death of the subject/donor and the time at which the specimen is made.</p>
</div>

<div id="left-hemisphere-preparation" class="field-detail">
<h5><code>left hemisphere preparation</code> <em>(required)</em></h5>
<ul>
<li><strong>BICAN UUID:</strong> <code>57d5378f-a451-4bf5-a472-cc88d0d29586</code></li>
<li><strong>Data Type:</strong> <code>exclusive_categorical</code></li>
<li><strong>Aliases:</strong> left_hemisphere_preparation</li>
</ul>
<p>The type of preparation method used for the left hemisphere.</p>
</div>

<div id="left-hemisphere-preparation-specify" class="field-detail">
<h5><code>left hemisphere preparation specify</code> <em>(required)</em></h5>
<ul>
<li><strong>BICAN UUID:</strong> <code>002e915e-01c3-4570-a1f3-76680dcb2c33</code></li>
<li><strong>Data Type:</strong> <code>text</code></li>
<li><strong>Aliases:</strong> left_hemisphere_preparation_specify</li>
</ul>
<p>Specific details about the type of preparation method used for the left hemisphere.</p>
</div>

<div id="right-hemisphere-preparation" class="field-detail">
<h5><code>right hemisphere preparation</code> <em>(required)</em></h5>
<ul>
<li><strong>BICAN UUID:</strong> <code>477c2600-f979-43c5-9c61-ab61fd771584</code></li>
<li><strong>Data Type:</strong> <code>exclusive_categorical</code></li>
<li><strong>Aliases:</strong> right_hemisphere_preparation</li>
</ul>
<p>The type of preparation method used for the right hemisphere.</p>
</div>

<div id="right-hemisphere-preparation-specify" class="field-detail">
<h5><code>right hemisphere preparation specify</code> <em>(required)</em></h5>
<ul>
<li><strong>BICAN UUID:</strong> <code>efd50be4-f7cf-4146-a08e-28f25680728c</code></li>
<li><strong>Data Type:</strong> <code>text</code></li>
<li><strong>Aliases:</strong> right_hemisphere_preparation_specify</li>
</ul>
<p>Specific details about the type of preparation method used for the right hemisphere.</p>
</div>

<div id="rin" class="field-detail">
<h5><code>RIN</code> <em>(required)</em></h5>
<ul>
<li><strong>BICAN UUID:</strong> <code>cd472c0d-0b64-45c9-a38e-e54d15cea953</code></li>
<li><strong>Data Type:</strong> <code>numeric</code></li>
<li><strong>Aliases:</strong> rin</li>
</ul>
<p>The RNA integrity number value of a specimen.</p>
</div>

<div id="rin-tissue-source" class="field-detail">
<h5><code>RIN tissue source</code> <em>(required)</em></h5>
<ul>
<li><strong>BICAN UUID:</strong> <code>d547ee51-9ec3-489c-8e49-7d8cd94080a8</code></li>
<li><strong>Data Type:</strong> <code>text</code></li>
<li><strong>Aliases:</strong> rin_tissue_source</li>
</ul>
<p>The tissue sample location or identifier that is used for calculating the RNA integrity number.</p>
</div>

<div id="rin-testing-organization" class="field-detail">
<h5><code>RIN testing organization</code> <em>(required)</em></h5>
<ul>
<li><strong>BICAN UUID:</strong> <code>cfed831e-9a62-4a32-bf92-532873420eb3</code></li>
<li><strong>Data Type:</strong> <code>text</code></li>
<li><strong>Aliases:</strong> rin_testing_organization</li>
</ul>
<p>The organization that determines the RNA integrity number of a sample/specimen.</p>
</div>

<div id="rine" class="field-detail">
<h5><code>RINe</code> <em>(required)</em></h5>
<ul>
<li><strong>BICAN UUID:</strong> <code>1210148d-d8fb-45aa-b51a-4b19b6d09bec</code></li>
<li><strong>Data Type:</strong> <code>numeric</code></li>
<li><strong>Aliases:</strong> rine</li>
</ul>
<p>A type of RIN (RNA integrity number) value that represents the relative ratio of the signal in the fast zone to the 18S peak signal fpr a specimen.</p>
</div>

<div id="rine-tissue-source" class="field-detail">
<h5><code>RINe tissue source</code> <em>(required)</em></h5>
<ul>
<li><strong>BICAN UUID:</strong> <code>7d5fd9af-82a1-4bdb-a3c6-9225d1717c53</code></li>
<li><strong>Data Type:</strong> <code>text</code></li>
<li><strong>Aliases:</strong> rine_tissue_source</li>
</ul>
<p>The tissue sample location or identifier that is used for calculating the RINe number.</p>
</div>

<div id="rine-testing-organization" class="field-detail">
<h5><code>RINe testing organization</code> <em>(required)</em></h5>
<ul>
<li><strong>BICAN UUID:</strong> <code>15a6d162-a3ca-4852-b626-a911c37c04c9</code></li>
<li><strong>Data Type:</strong> <code>text</code></li>
<li><strong>Aliases:</strong> rine_testing_organization</li>
</ul>
<p>The organization that determines the RINe number.</p>
</div>

<div id="ph" class="field-detail">
<h5><code>pH</code> <em>(required)</em></h5>
<ul>
<li><strong>BICAN UUID:</strong> <code>9e67af02-c081-43e1-a42c-bf9603cae616</code></li>
<li><strong>Data Type:</strong> <code>numeric</code></li>
<li><strong>Aliases:</strong> ph</li>
</ul>
<p>The value of a measurement of acidity or basicity of a tissue, sample, or specimen.</p>
</div>

<div id="brain-weight-measurement" class="field-detail">
<h5><code>brain weight measurement</code> <em>(required)</em></h5>
<ul>
<li><strong>BICAN UUID:</strong> <code>546fc32d-f8a2-4c00-924a-8c4730f11f51</code></li>
<li><strong>Data Type:</strong> <code>numeric</code></li>
<li><strong>Aliases:</strong> brain_weight</li>
</ul>
<p>The weight of a brain specimen.</p>
</div>

<div id="brain-tissue-weighed-type" class="field-detail">
<h5><code>brain tissue weighed type</code> <em>(required)</em></h5>
<ul>
<li><strong>BICAN UUID:</strong> <code>a7463e3f-0c61-4718-a7d0-60fd2116908a</code></li>
<li><strong>Data Type:</strong> <code>exclusive_categorical</code></li>
<li><strong>Aliases:</strong> weighed_type</li>
</ul>
<p>The state of a brain specimen when it is weighed (fresh, frozen, fixed).</p>
</div>

<div id="photo-2d-available" class="field-detail">
<h5><code>photo 2d available</code> <em>(required)</em></h5>
<ul>
<li><strong>BICAN UUID:</strong> <code>611beda8-1ac6-4183-a284-04a30bb474f3</code></li>
<li><strong>Data Type:</strong> <code>exclusive_categorical</code></li>
<li><strong>Aliases:</strong> photo_2d_available</li>
</ul>
<p>The status (available, unavailable) of two-dimensional photos of a subject/donor/specimen.</p>
</div>

<div id="scan-3d-available" class="field-detail">
<h5><code>scan 3d available</code> <em>(required)</em></h5>
<ul>
<li><strong>BICAN UUID:</strong> <code>658e8a80-e232-438f-8c1e-d5f38724dc55</code></li>
<li><strong>Data Type:</strong> <code>exclusive_categorical</code></li>
<li><strong>Aliases:</strong> scan_3d_available</li>
</ul>
<p>The status (available, unavailable) of three-dimensional scans of a subject/donor/specimen.</p>
</div>

<div id="antemortem-mri-available" class="field-detail">
<h5><code>antemortem MRI available</code> <em>(required)</em></h5>
<ul>
<li><strong>BICAN UUID:</strong> <code>43a04caa-4f28-47ac-8a9d-74c40f10776f</code></li>
<li><strong>Data Type:</strong> <code>exclusive_categorical</code></li>
<li><strong>Aliases:</strong> antemortem_mri_available</li>
</ul>
<p>The status (available, unavailable) of antemortem MRI images of a subject/donor/specimen.</p>
</div>

<div id="postmortem-mri-available" class="field-detail">
<h5><code>postmortem MRI available</code> <em>(required)</em></h5>
<ul>
<li><strong>BICAN UUID:</strong> <code>0badd072-0c25-48c6-9357-44d5b5bc0818</code></li>
<li><strong>Data Type:</strong> <code>exclusive_categorical</code></li>
<li><strong>Aliases:</strong> postmortem_mri_available</li>
</ul>
<p>The status (available, unavailable) of postmortem MRI images of a subject/donor/specimen.</p>
</div>

<div id="postmortem-mri-type" class="field-detail">
<h5><code>postmortem MRI type</code> <em>(optional)</em></h5>
<ul>
<li><strong>BICAN UUID:</strong> <code>64a607a9-21e6-4c73-8f2e-2d67b0dc51c8</code></li>
<li><strong>Data Type:</strong> <code>exclusive_categorical</code></li>
<li><strong>Aliases:</strong> postmortem_mri_type</li>
</ul>
<p>The type of postmortem MRI that is available (cadeveric, fresh ex vivo, fixed ex vivo).</p>
</div>

<div id="premortem-perfusion-done" class="field-detail">
<h5><code>premortem perfusion done</code> <em>(required)</em></h5>
<ul>
<li><strong>BICAN UUID:</strong> <code>1fc487d8-2403-4d7c-952f-7e502d5f8359</code></li>
<li><strong>Data Type:</strong> <code>exclusive_categorical</code></li>
<li><strong>Aliases:</strong> perfusion</li>
</ul>
<p>The status of premortem perfusion (done, not done).</p>
</div>

<div id="premortem-perfusion-buffer-type" class="field-detail">
<h5><code>premortem perfusion buffer type</code> <em>(optional)</em></h5>
<ul>
<li><strong>BICAN UUID:</strong> <code>78d62e29-4323-4927-aec8-6fc8dc59a889</code></li>
<li><strong>Data Type:</strong> <code>text</code></li>
<li><strong>Aliases:</strong> perfusate_type</li>
</ul>
<p>The type of premortem perfusion buffer that was used for premortem perfusion.</p>
</div>

<div id="head-off-time" class="field-detail">
<h5><code>head off time</code> <em>(required)</em></h5>
<ul>
<li><strong>BICAN UUID:</strong> <code>00ab5986-a8c4-4a7f-bf2b-6b5f08a97b25</code></li>
<li><strong>Data Type:</strong> <code>time</code></li>
<li><strong>Aliases:</strong> head_off_time</li>
</ul>
<p>The time at which the head was removed from the organism/donor/subject.</p>
</div>

<div id="brain-extraction-time" class="field-detail">
<h5><code>brain extraction time</code> <em>(required)</em></h5>
<ul>
<li><strong>BICAN UUID:</strong> <code>06be5810-7b9c-452e-b7ca-13eeb15179ca</code></li>
<li><strong>Data Type:</strong> <code>time</code></li>
<li><strong>Aliases:</strong> brain_extraction_time</li>
</ul>
<p>The time at which the brain was extracted from the organism/donor/subject.</p>
</div>

<div id="brain-fixed-time" class="field-detail">
<h5><code>brain fixed time</code> <em>(optional)</em></h5>
<ul>
<li><strong>BICAN UUID:</strong> <code>2a09ecb4-0096-4a6c-b4f0-9b68cb231413</code></li>
<li><strong>Data Type:</strong> <code>time</code></li>
<li><strong>Aliases:</strong> brain_fixed_time</li>
</ul>
<p>The time at which the brain specimen was fixed.</p>
</div>

<div id="brain-frozen-time" class="field-detail">
<h5><code>brain frozen time</code> <em>(optional)</em></h5>
<ul>
<li><strong>BICAN UUID:</strong> <code>fb01ce0d-1417-404a-978d-aad708c0404f</code></li>
<li><strong>Data Type:</strong> <code>time</code></li>
<li><strong>Aliases:</strong> brain_frozen_time</li>
</ul>
<p>The time at which the brain specimen was frozen.</p>
</div>

<div id="brain-fixation-method" class="field-detail">
<h5><code>brain fixation method</code> <em>(optional)</em></h5>
<ul>
<li><strong>BICAN UUID:</strong> <code>8e0a01a9-ab7a-49a5-bf44-cc0af47719b1</code></li>
<li><strong>Data Type:</strong> <code>exclusive_categorical</code></li>
<li><strong>Aliases:</strong> brain_fixation_method</li>
</ul>
<p>The method used for fixing the brain specimen.</p>
</div>

<div id="brain-freeze-method" class="field-detail">
<h5><code>brain freeze method</code> <em>(optional)</em></h5>
<ul>
<li><strong>BICAN UUID:</strong> <code>71237def-9b50-481f-a01d-65dc99e3493f</code></li>
<li><strong>Data Type:</strong> <code>exclusive_categorical</code></li>
<li><strong>Aliases:</strong> brain_freeze_method</li>
</ul>
<p>The method used for freezing the brain specimen.</p>
</div>

<div id="sedation-start-time" class="field-detail">
<h5><code>sedation start time</code> <em>(required)</em></h5>
<ul>
<li><strong>BICAN UUID:</strong> <code>0ad6cca0-d4ce-4cd8-bbce-520bc01db061</code></li>
<li><strong>Data Type:</strong> <code>time</code></li>
<li><strong>Aliases:</strong> sedation_start_time</li>
</ul>
<p>The time at which sedation of the organism/donor/subject began.</p>
</div>

<div id="sedation-total-dose" class="field-detail">
<h5><code>sedation total dose</code> <em>(required)</em></h5>
<ul>
<li><strong>BICAN UUID:</strong> <code>3c895613-4526-4b87-8620-7b42eff94fee</code></li>
<li><strong>Data Type:</strong> <code>numeric</code></li>
<li><strong>Aliases:</strong> sedation_total_dose</li>
</ul>
<p>The total dose of sedation used on the organism/donor/subject.</p>
</div>

<div id="euthanasia-time" class="field-detail">
<h5><code>euthanasia time</code> <em>(required)</em></h5>
<ul>
<li><strong>BICAN UUID:</strong> <code>14c541ab-7db3-4438-9328-c5f3098f5ff7</code></li>
<li><strong>Data Type:</strong> <code>time</code></li>
<li><strong>Aliases:</strong> euthanasia_time</li>
</ul>
<p>The time at which euthanasia of the organism/donor/subject occurred.</p>
</div>

<div id="euthanasia-dose" class="field-detail">
<h5><code>euthanasia dose</code> <em>(required)</em></h5>
<ul>
<li><strong>BICAN UUID:</strong> <code>d87c6869-c0d1-46b3-bb32-95dc3e3d5ed4</code></li>
<li><strong>Data Type:</strong> <code>numeric</code></li>
<li><strong>Aliases:</strong> euthanasia_dose</li>
</ul>
<p>The dose of compouds used to euthanize the organism/donor/subject.</p>
</div>

<div id="perfusion-time-start" class="field-detail">
<h5><code>perfusion time start</code> <em>(required)</em></h5>
<ul>
<li><strong>BICAN UUID:</strong> <code>7f94f8ad-82b7-4827-9614-838555a1f046</code></li>
<li><strong>Data Type:</strong> <code>time</code></li>
<li><strong>Aliases:</strong> perfusion_time_start</li>
</ul>
<p>The time at which perfusion began.</p>
</div>

<div id="perfusion-time-end" class="field-detail">
<h5><code>perfusion time end</code> <em>(required)</em></h5>
<ul>
<li><strong>BICAN UUID:</strong> <code>6c873444-8306-4b3f-9e5a-97f6d34c88b3</code></li>
<li><strong>Data Type:</strong> <code>time</code></li>
<li><strong>Aliases:</strong> perfusion_time_end</li>
</ul>
<p>The time at which perfusion ended.</p>
</div>

<div id="brain-size-anterior-posterior" class="field-detail">
<h5><code>brain size anterior-posterior</code> <em>(required)</em></h5>
<ul>
<li><strong>BICAN UUID:</strong> <code>0830564a-26ba-41eb-888a-33d0c39ead8f</code></li>
<li><strong>Data Type:</strong> <code>numeric</code></li>
<li><strong>Aliases:</strong> brain_size_anterior_posterior</li>
</ul>
<p>The size of the brain specimen in the anterior-posterior axis.</p>
</div>

<div id="brain-size-medial-lateral" class="field-detail">
<h5><code>brain size medial-lateral</code> <em>(required)</em></h5>
<ul>
<li><strong>BICAN UUID:</strong> <code>4722f739-71f6-4001-9784-afef8f9f2d0e</code></li>
<li><strong>Data Type:</strong> <code>numeric</code></li>
<li><strong>Aliases:</strong> brain_size_medial_lateral</li>
</ul>
<p>The size of the brain specimen in the medial-lateral axis.</p>
</div>

<div id="brain-size-dorsal-ventral" class="field-detail">
<h5><code>brain size dorsal-ventral</code> <em>(required)</em></h5>
<ul>
<li><strong>BICAN UUID:</strong> <code>e683f5ee-696f-4baf-a9bf-2f12226ceb4a</code></li>
<li><strong>Data Type:</strong> <code>numeric</code></li>
<li><strong>Aliases:</strong> brain_size_dorsal_ventral</li>
</ul>
<p>The size of the brain specimen in the dorsal-ventral axis.</p>
</div>

<div id="brain-size-unit" class="field-detail">
<h5><code>brain size unit</code> <em>(required)</em></h5>
<ul>
<li><strong>BICAN UUID:</strong> <code>4d0c44c6-e620-455d-989e-126c3c81ec91</code></li>
<li><strong>Data Type:</strong> <code>exclusive_categorical</code></li>
<li><strong>Aliases:</strong> brain_size_unit_type</li>
</ul>
<p>The unit that the brain size measurements are recorded.</p>
</div>

<div id="histological-stains-available" class="field-detail">
<h5><code>histological stains available</code> <em>(required)</em></h5>
<ul>
<li><strong>BICAN UUID:</strong> <code>4b868ba6-dba8-45e3-a43e-88e421625cab</code></li>
<li><strong>Data Type:</strong> <code>exclusive_categorical</code></li>
<li><strong>Aliases:</strong> histological_stains_available</li>
</ul>
<p>The status (available, unavailable) of histological stainings of a specimen.</p>
</div>

<div id="histological-stains-type" class="field-detail">
<h5><code>histological stains type</code> <em>(optional)</em></h5>
<ul>
<li><strong>BICAN UUID:</strong> <code>6723e756-e4c1-42c7-bf2d-ee2e300b88ff</code></li>
<li><strong>Data Type:</strong> <code>exclusive_categorical</code></li>
<li><strong>Aliases:</strong> histological_stain_type</li>
</ul>
<p>The type of histological stains available for a specimen.</p>
</div>

#### General Subject Fields

<div id="local-donor-id" class="field-detail">
<h5><code>local donor ID</code> <em>(required)</em></h5>
<ul>
<li><strong>BICAN UUID:</strong> <code>f8af20f7-e8b8-47b5-8a68-9ec1f913ffdf</code></li>
<li><strong>Data Type:</strong> <code>text</code></li>
<li><strong>Aliases:</strong> subject_id</li>
</ul>
<p>An identifier that uniquely denotes objects only within the scope of a specific object aggregate and that is not registered in an identifier registry. [Allotrope]</p>
</div>

<div id="repository" class="field-detail">
<h5><code>repository</code> <em>(required)</em></h5>
<ul>
<li><strong>BICAN UUID:</strong> <code>408682ed-0e27-41e2-b9fa-f05674366d6e</code></li>
<li><strong>Data Type:</strong> <code>inclusive_categorical</code></li>
<li><strong>Aliases:</strong> repository</li>
</ul>
<p>&#x27;Repository&#x27; trailing modifier (qualifier, &#x27;repository&#x27;) of &#x27;xref&#x27; links of &#x27;Format&#x27; concepts. When &#x27;true&#x27;, the link is pointing to the public source-code repository where the given data format is developed or maintained. [EDAM]</p>
</div>

<div id="donor-source" class="field-detail">
<h5><code>donor source</code> <em>(required)</em></h5>
<ul>
<li><strong>BICAN UUID:</strong> <code>0d0cf732-0f76-409d-9a73-7a96d829d3d3</code></li>
<li><strong>Data Type:</strong> <code>inclusive_categorical</code></li>
<li><strong>Aliases:</strong> donor_source</li>
</ul>
<p>The origin of the donor/subject in this experiment.</p>
</div>

<div id="sex-at-birth" class="field-detail">
<h5><code>sex at birth</code> <em>(required)</em></h5>
<ul>
<li><strong>BICAN UUID:</strong> <code>c819b9d5-2fde-40b2-bf0d-e07b56f96ac9</code></li>
<li><strong>Data Type:</strong> <code>exclusive_categorical</code></li>
<li><strong>Aliases:</strong> sex</li>
</ul>
<p>An organismal quality inhering in a bearer by virtue of the bearer&#x27;s ability to undergo sexual reproduction in order to differentiate the individuals or types involved. [PATO]</p>
</div>

<div id="age-value-(years)" class="field-detail">
<h5><code>age value (years)</code> <em>(required)</em></h5>
<ul>
<li><strong>BICAN UUID:</strong> <code>14eb923a-161d-45e2-889d-81fea7b632b6</code></li>
<li><strong>Data Type:</strong> <code>numeric</code></li>
<li><strong>Aliases:</strong> age_of_death</li>
</ul>
<p>A time quality inhering in a bearer by virtue of how long the bearer has existed. [PATO]</p>
</div>

<div id="year-of-death" class="field-detail">
<h5><code>year of death</code> <em>(required)</em></h5>
<ul>
<li><strong>BICAN UUID:</strong> <code>60445046-d9d8-4f00-959e-9a4c42613e5e</code></li>
<li><strong>Data Type:</strong> <code>date</code></li>
<li><strong>Aliases:</strong> year_of_death</li>
</ul>
<p>The year wherein the subject or donor has ceased to exist.</p>
</div>

<div id="autopsy-report" class="field-detail">
<h5><code>autopsy report</code> <em>(required)</em></h5>
<ul>
<li><strong>BICAN UUID:</strong> <code>3f787b64-0985-4d0f-9523-54475164b7ad</code></li>
<li><strong>Data Type:</strong> <code>exclusive_categorical</code></li>
<li><strong>Aliases:</strong> autopsy_report</li>
</ul>
<p>A document assembled by an author for the purpose of providing information regarding the cause of death of a subject for the audience. [IAO, modified]</p>
</div>

<div id="cause-of-death" class="field-detail">
<h5><code>cause of death</code> <em>(required)</em></h5>
<ul>
<li><strong>BICAN UUID:</strong> <code>fa970a03-41ea-473b-a8ce-427fec92cdff</code></li>
<li><strong>Data Type:</strong> <code>text</code></li>
<li><strong>Aliases:</strong> cause_of_death</li>
</ul>
<p>The circumstance or condition that results in the death of a living being. [NCIT]</p>
</div>

<div id="cause-of-death-code" class="field-detail">
<h5><code>cause of death code</code> <em>(required)</em></h5>
<ul>
<li><strong>BICAN UUID:</strong> <code>61374624-2d3c-477e-95b3-9bd30974b52a</code></li>
<li><strong>Data Type:</strong> <code>text</code></li>
<li><strong>Aliases:</strong> cause_of_death_code</li>
</ul>
<p>The ISO code that denotes the circumstance or condition that results in the death of a living being. [NCIT]</p>
</div>

<div id="manner-of-death" class="field-detail">
<h5><code>manner of death</code> <em>(required)</em></h5>
<ul>
<li><strong>BICAN UUID:</strong> <code>36eeb35b-5020-4a9e-a74b-6e1104415e0e</code></li>
<li><strong>Data Type:</strong> <code>exclusive_categorical</code></li>
<li><strong>Aliases:</strong> manner_of_death</li>
</ul>
<p>The manner of death is the determination of how the injury or disease leads to death.  There are five manners of death (natural, accident, suicide, homicide, and undetermined).</p>
</div>

<div id="medical-records-reviewed" class="field-detail">
<h5><code>medical records reviewed</code> <em>(required)</em></h5>
<ul>
<li><strong>BICAN UUID:</strong> <code>6139b159-c36c-4501-9176-fe2741e3d448</code></li>
<li><strong>Data Type:</strong> <code>exclusive_categorical</code></li>
<li><strong>Aliases:</strong> medical_records_reviewed</li>
</ul>
<p>The status (reviewed, not reviewed) of the medical records of the subject/donor.</p>
</div>

<div id="species" class="field-detail">
<h5><code>species</code> <em>(required)</em></h5>
<ul>
<li><strong>BICAN UUID:</strong> <code>d11fb2ce-bfdb-4735-9b17-b6ba606520b1</code></li>
<li><strong>Data Type:</strong> <code>exclusive_categorical</code></li>
<li><strong>Aliases:</strong> species</li>
</ul>
<p>The species of a subject/donor/sample/specimen.</p>
</div>

<div id="social-group" class="field-detail">
<h5><code>social group</code> <em>(required)</em></h5>
<ul>
<li><strong>BICAN UUID:</strong> <code>7759b09d-a685-49fe-b7d8-e7f2b4772f52</code></li>
<li><strong>Data Type:</strong> <code>exclusive_categorical</code></li>
<li><strong>Aliases:</strong> social_group</li>
</ul>
<p>The social group to which the subject belongs.</p>
</div>

<div id="body-weight" class="field-detail">
<h5><code>body weight</code> <em>(required)</em></h5>
<ul>
<li><strong>BICAN UUID:</strong> <code>f2673501-b48f-4703-bb7e-d642b73c2ad4</code></li>
<li><strong>Data Type:</strong> <code>numeric</code></li>
<li><strong>Aliases:</strong> body_weight</li>
</ul>
<p>The weight of the whole organism/donor/subject.</p>
</div>

#### Infant Medical History

<div id="birth-weight-value-(lbs)" class="field-detail">
<h5><code>birth weight value (lbs)</code> <em>(required)</em></h5>
<ul>
<li><strong>BICAN UUID:</strong> <code>69d9a60d-32d5-4c3a-a26a-802d8f030c8d</code></li>
<li><strong>Data Type:</strong> <code>numeric</code></li>
<li><strong>Aliases:</strong> birth_weight_lbs</li>
</ul>
<p>The weight (at birth) of the subject/donor in pounds.</p>
</div>

<div id="birth-weight-value-(oz)" class="field-detail">
<h5><code>birth weight value (oz)</code> <em>(required)</em></h5>
<ul>
<li><strong>BICAN UUID:</strong> <code>b6f30050-f762-4427-8533-31738e737ea2</code></li>
<li><strong>Data Type:</strong> <code>numeric</code></li>
<li><strong>Aliases:</strong> birth_weight_oz</li>
</ul>
<p>The weight (at birth) of the subject/donor in ounces.</p>
</div>

<div id="gestational-age-value-(weeks)" class="field-detail">
<h5><code>gestational age value (weeks)</code> <em>(required)</em></h5>
<ul>
<li><strong>BICAN UUID:</strong> <code>6d8a9b3f-792c-48c2-bd3c-56e52bb51672</code></li>
<li><strong>Data Type:</strong> <code>numeric</code></li>
<li><strong>Aliases:</strong> gestational_age_value_weeks</li>
</ul>
<p>The gestational age of the subject/donor in weeks.</p>
</div>

<div id="gestational-age-value-(days)" class="field-detail">
<h5><code>gestational age value (days)</code> <em>(required)</em></h5>
<ul>
<li><strong>BICAN UUID:</strong> <code>4e532e52-6e4c-46cd-9fde-96f97ef3b034</code></li>
<li><strong>Data Type:</strong> <code>numeric</code></li>
<li><strong>Aliases:</strong> gestational_age_value_days</li>
</ul>
<p>The gestational age of the subject/donor in days.</p>
</div>

#### Non-Brain Specimen Collected

<div id="non-brain-tissue-available" class="field-detail">
<h5><code>non-brain tissue available</code> <em>(required)</em></h5>
<ul>
<li><strong>BICAN UUID:</strong> <code>3a064c96-a956-4cf3-8b77-056b8e392f99</code></li>
<li><strong>Data Type:</strong> <code>exclusive_categorical</code></li>
<li><strong>Aliases:</strong> non_brain_tissue_available</li>
</ul>
<p>The status (yes, no) of whether non-brain tissue from this organism is available.</p>
</div>

<div id="tissue-type" class="field-detail">
<h5><code>tissue type</code> <em>(required)</em></h5>
<ul>
<li><strong>BICAN UUID:</strong> <code>33ccbc85-ae35-44d6-8bc6-c2fb91116cf7</code></li>
<li><strong>Data Type:</strong> <code>exclusive_categorical</code></li>
<li><strong>Aliases:</strong> tissue_type</li>
</ul>
<p>The type of tissue (non-brain) that is available from this organism.</p>
</div>

<div id="tissue-type-details" class="field-detail">
<h5><code>tissue type details</code> <em>(optional)</em></h5>
<ul>
<li><strong>BICAN UUID:</strong> <code>f551cf87-2c6e-4b92-888d-6310e6a500d8</code></li>
<li><strong>Data Type:</strong> <code>text</code></li>
<li><strong>Aliases:</strong> tissue_type_details</li>
</ul>
<p>The details of the non-brain tissue that is available from this organism.</p>
</div>

<!-- schema-properties-end:population -->

<!-- schema-properties-start:patchseq -->
## Patchseq properties
*Auto-generated from CSV. Do not edit this section manually.*

**Status:** Accepted by MOWG &middot; **Version:** 1.0.0 &middot; **Date:** 2024-07-08

### Properties

#### Diagnoses

| Property | Type | Required | Aliases | Description |
|----------|------|----------|---------|-------------|
| [`non brain diagnosis description`](#non-brain-diagnosis-description) | text | no | non_brain_diagnosis_description | The description (text) of a non-brain diagnosis for a subject/donor/specimen. |

#### General Specimen Data

| Property | Type | Required | Aliases | Description |
|----------|------|----------|---------|-------------|
| [`hemisphere`](#hemisphere) | exclusive_categorical | yes | hemisphere | One of two bilateral, largely symmetrical organ subdivisions within the telencephalon which contain the cerebral cortex … |
| [`post mortem interval`](#post-mortem-interval) | numeric | yes | post_mortem_interval | The length of the temporal interval between the time of death of the subject/donor and the time at which the specimen is… |
| [`left hemisphere preparation`](#left-hemisphere-preparation) | exclusive_categorical | yes | left_hemisphere_preparation | The type of preparation method used for the left hemisphere. |
| [`left hemisphere preparation specify`](#left-hemisphere-preparation-specify) | text | yes | left_hemisphere_preparation_specify | Specific details about the type of preparation method used for the left hemisphere. |
| [`right hemisphere preparation`](#right-hemisphere-preparation) | exclusive_categorical | yes | right_hemisphere_preparation | The type of preparation method used for the right hemisphere. |
| [`right hemisphere preparation specify`](#right-hemisphere-preparation-specify) | text | yes | right_hemisphere_preparation_specify | Specific details about the type of preparation method used for the right hemisphere. |
| [`photo 2d available`](#photo-2d-available) | exclusive_categorical | yes | photo_2d_available | The status (available, unavailable) of two-dimensional photos of a subject/donor/specimen. |
| [`antemortem MRI available`](#antemortem-mri-available) | exclusive_categorical | yes | antemortem_mri_available | The status (available, unavailable) of antemortem MRI images of a subject/donor/specimen. |
| [`premortem perfusion done`](#premortem-perfusion-done) | exclusive_categorical | yes | perfusion | The status of premortem perfusion (done, not done). |
| [`premortem perfusion buffer type`](#premortem-perfusion-buffer-type) | text | no | perfusate_type | The type of premortem perfusion buffer that was used for premortem perfusion. |
| [`region of interest`](#region-of-interest) | exclusive_categorical | yes | ROI | The brain region, structure, or area from which a brain tissue source derives. |

#### General Subject Fields

| Property | Type | Required | Aliases | Description |
|----------|------|----------|---------|-------------|
| [`local donor ID`](#local-donor-id) | text | yes | subject_id | An identifier that uniquely denotes objects only within the scope of a specific object aggregate and that is not registe… |
| [`repository`](#repository) | inclusive_categorical | yes | repository | &#x27;Repository&#x27; trailing modifier (qualifier, &#x27;repository&#x27;) of &#x27;xref&#x27; links of &#x27;Format&#x27; concepts. When &#x27;true&#x27;, the link is … |
| [`donor source`](#donor-source) | inclusive_categorical | yes | donor_source | The origin of the donor/subject in this experiment. |
| [`sex at birth`](#sex-at-birth) | exclusive_categorical | yes | sex | An organismal quality inhering in a bearer by virtue of the bearer&#x27;s ability to undergo sexual reproduction in order to … |
| [`age value (years)`](#age-value-(years)) | numeric | yes | age_of_death | A time quality inhering in a bearer by virtue of how long the bearer has existed. [PATO] |
| [`year of death`](#year-of-death) | date | yes | year_of_death | The year wherein the subject or donor has ceased to exist. |
| [`manner of death`](#manner-of-death) | exclusive_categorical | yes | manner_of_death | The manner of death is the determination of how the injury or disease leads to death.  There are five manners of death (… |
| [`medical records available`](#medical-records-available) | exclusive_categorical | yes | medical_records_available | The status (available, unavailable) of the medical records of the subject/donor. |
| [`medical records reviewed`](#medical-records-reviewed) | exclusive_categorical | no | medical_records_reviewed | The status (reviewed, not reviewed) of the medical records of the subject/donor. |
| [`species`](#species) | exclusive_categorical | yes | species | The species of a subject/donor/sample/specimen. |
| [`behavioral scoring available`](#behavioral-scoring-available) | exclusive_categorical | yes | behavioral_scoring_available | The status (available, unavailable) of the behavioral scoring results for a subject/donor/specimen. |
| [`behavioral scoring type`](#behavioral-scoring-type) | text | no | behavioral_scoring_type | The type of behavioral scoring that is available for a subject/donor/specimen. |

#### Infectious Disease Testing

| Property | Type | Required | Aliases | Description |
|----------|------|----------|---------|-------------|
| [`test name`](#test-name) | exclusive_categorical | no | test_name | The name of the test that has been performed. |
| [`test result`](#test-result) | exclusive_categorical | no | test_result | The result(s) of the test that has been performed. |
| [`testing tissue source`](#testing-tissue-source) | exclusive_categorical | yes | tissue_source | The tissue sample location or identifier that is the subject of a test. |

#### Non-Brain Specimen Collected

| Property | Type | Required | Aliases | Description |
|----------|------|----------|---------|-------------|
| [`non-brain tissue available`](#non-brain-tissue-available) | exclusive_categorical | yes | non_brain_tissue_available | The status (yes, no) of whether non-brain tissue from this organism is available. |
| [`tissue type`](#tissue-type) | exclusive_categorical | yes | tissue_type | The type of tissue (non-brain) that is available from this organism. |
| [`tissue type details`](#tissue-type-details) | text | no | tissue_type_details | The details of the non-brain tissue that is available from this organism. |

### Property Details

#### Diagnoses

<div id="non-brain-diagnosis-description" class="field-detail">
<h5><code>non brain diagnosis description</code> <em>(optional)</em></h5>
<ul>
<li><strong>BICAN UUID:</strong> <code>4ba7c8cc-563c-4f0b-ab57-ae9c9762943f</code></li>
<li><strong>Data Type:</strong> <code>text</code></li>
<li><strong>Aliases:</strong> non_brain_diagnosis_description</li>
</ul>
<p>The description (text) of a non-brain diagnosis for a subject/donor/specimen.</p>
</div>

#### General Specimen Data

<div id="hemisphere" class="field-detail">
<h5><code>hemisphere</code> <em>(required)</em></h5>
<ul>
<li><strong>BICAN UUID:</strong> <code>68b7a28b-d695-4ec9-800b-6a27ca206081</code></li>
<li><strong>Data Type:</strong> <code>exclusive_categorical</code></li>
<li><strong>Aliases:</strong> hemisphere</li>
</ul>
<p>One of two bilateral, largely symmetrical organ subdivisions within the telencephalon which contain the cerebral cortex and cerebral white matter. [UBERON]</p>
</div>

<div id="post-mortem-interval" class="field-detail">
<h5><code>post mortem interval</code> <em>(required)</em></h5>
<ul>
<li><strong>BICAN UUID:</strong> <code>6fd5c5ac-b128-4a4a-ae98-09eaeba22f92</code></li>
<li><strong>Data Type:</strong> <code>numeric</code></li>
<li><strong>Aliases:</strong> post_mortem_interval</li>
</ul>
<p>The length of the temporal interval between the time of death of the subject/donor and the time at which the specimen is made.</p>
</div>

<div id="left-hemisphere-preparation" class="field-detail">
<h5><code>left hemisphere preparation</code> <em>(required)</em></h5>
<ul>
<li><strong>BICAN UUID:</strong> <code>57d5378f-a451-4bf5-a472-cc88d0d29586</code></li>
<li><strong>Data Type:</strong> <code>exclusive_categorical</code></li>
<li><strong>Aliases:</strong> left_hemisphere_preparation</li>
</ul>
<p>The type of preparation method used for the left hemisphere.</p>
</div>

<div id="left-hemisphere-preparation-specify" class="field-detail">
<h5><code>left hemisphere preparation specify</code> <em>(required)</em></h5>
<ul>
<li><strong>BICAN UUID:</strong> <code>002e915e-01c3-4570-a1f3-76680dcb2c33</code></li>
<li><strong>Data Type:</strong> <code>text</code></li>
<li><strong>Aliases:</strong> left_hemisphere_preparation_specify</li>
</ul>
<p>Specific details about the type of preparation method used for the left hemisphere.</p>
</div>

<div id="right-hemisphere-preparation" class="field-detail">
<h5><code>right hemisphere preparation</code> <em>(required)</em></h5>
<ul>
<li><strong>BICAN UUID:</strong> <code>477c2600-f979-43c5-9c61-ab61fd771584</code></li>
<li><strong>Data Type:</strong> <code>exclusive_categorical</code></li>
<li><strong>Aliases:</strong> right_hemisphere_preparation</li>
</ul>
<p>The type of preparation method used for the right hemisphere.</p>
</div>

<div id="right-hemisphere-preparation-specify" class="field-detail">
<h5><code>right hemisphere preparation specify</code> <em>(required)</em></h5>
<ul>
<li><strong>BICAN UUID:</strong> <code>efd50be4-f7cf-4146-a08e-28f25680728c</code></li>
<li><strong>Data Type:</strong> <code>text</code></li>
<li><strong>Aliases:</strong> right_hemisphere_preparation_specify</li>
</ul>
<p>Specific details about the type of preparation method used for the right hemisphere.</p>
</div>

<div id="photo-2d-available" class="field-detail">
<h5><code>photo 2d available</code> <em>(required)</em></h5>
<ul>
<li><strong>BICAN UUID:</strong> <code>611beda8-1ac6-4183-a284-04a30bb474f3</code></li>
<li><strong>Data Type:</strong> <code>exclusive_categorical</code></li>
<li><strong>Aliases:</strong> photo_2d_available</li>
</ul>
<p>The status (available, unavailable) of two-dimensional photos of a subject/donor/specimen.</p>
</div>

<div id="antemortem-mri-available" class="field-detail">
<h5><code>antemortem MRI available</code> <em>(required)</em></h5>
<ul>
<li><strong>BICAN UUID:</strong> <code>43a04caa-4f28-47ac-8a9d-74c40f10776f</code></li>
<li><strong>Data Type:</strong> <code>exclusive_categorical</code></li>
<li><strong>Aliases:</strong> antemortem_mri_available</li>
</ul>
<p>The status (available, unavailable) of antemortem MRI images of a subject/donor/specimen.</p>
</div>

<div id="premortem-perfusion-done" class="field-detail">
<h5><code>premortem perfusion done</code> <em>(required)</em></h5>
<ul>
<li><strong>BICAN UUID:</strong> <code>1fc487d8-2403-4d7c-952f-7e502d5f8359</code></li>
<li><strong>Data Type:</strong> <code>exclusive_categorical</code></li>
<li><strong>Aliases:</strong> perfusion</li>
</ul>
<p>The status of premortem perfusion (done, not done).</p>
</div>

<div id="premortem-perfusion-buffer-type" class="field-detail">
<h5><code>premortem perfusion buffer type</code> <em>(optional)</em></h5>
<ul>
<li><strong>BICAN UUID:</strong> <code>78d62e29-4323-4927-aec8-6fc8dc59a889</code></li>
<li><strong>Data Type:</strong> <code>text</code></li>
<li><strong>Aliases:</strong> perfusate_type</li>
</ul>
<p>The type of premortem perfusion buffer that was used for premortem perfusion.</p>
</div>

<div id="region-of-interest" class="field-detail">
<h5><code>region of interest</code> <em>(required)</em></h5>
<ul>
<li><strong>BICAN UUID:</strong> <code>71611b58-f98e-4a69-ad88-c0029a377cbe</code></li>
<li><strong>Data Type:</strong> <code>exclusive_categorical</code></li>
<li><strong>Aliases:</strong> ROI</li>
</ul>
<p>The brain region, structure, or area from which a brain tissue source derives.</p>
</div>

#### General Subject Fields

<div id="local-donor-id" class="field-detail">
<h5><code>local donor ID</code> <em>(required)</em></h5>
<ul>
<li><strong>BICAN UUID:</strong> <code>f8af20f7-e8b8-47b5-8a68-9ec1f913ffdf</code></li>
<li><strong>Data Type:</strong> <code>text</code></li>
<li><strong>Aliases:</strong> subject_id</li>
</ul>
<p>An identifier that uniquely denotes objects only within the scope of a specific object aggregate and that is not registered in an identifier registry. [Allotrope]</p>
</div>

<div id="repository" class="field-detail">
<h5><code>repository</code> <em>(required)</em></h5>
<ul>
<li><strong>BICAN UUID:</strong> <code>408682ed-0e27-41e2-b9fa-f05674366d6e</code></li>
<li><strong>Data Type:</strong> <code>inclusive_categorical</code></li>
<li><strong>Aliases:</strong> repository</li>
</ul>
<p>&#x27;Repository&#x27; trailing modifier (qualifier, &#x27;repository&#x27;) of &#x27;xref&#x27; links of &#x27;Format&#x27; concepts. When &#x27;true&#x27;, the link is pointing to the public source-code repository where the given data format is developed or maintained. [EDAM]</p>
</div>

<div id="donor-source" class="field-detail">
<h5><code>donor source</code> <em>(required)</em></h5>
<ul>
<li><strong>BICAN UUID:</strong> <code>0d0cf732-0f76-409d-9a73-7a96d829d3d3</code></li>
<li><strong>Data Type:</strong> <code>inclusive_categorical</code></li>
<li><strong>Aliases:</strong> donor_source</li>
</ul>
<p>The origin of the donor/subject in this experiment.</p>
</div>

<div id="sex-at-birth" class="field-detail">
<h5><code>sex at birth</code> <em>(required)</em></h5>
<ul>
<li><strong>BICAN UUID:</strong> <code>c819b9d5-2fde-40b2-bf0d-e07b56f96ac9</code></li>
<li><strong>Data Type:</strong> <code>exclusive_categorical</code></li>
<li><strong>Aliases:</strong> sex</li>
</ul>
<p>An organismal quality inhering in a bearer by virtue of the bearer&#x27;s ability to undergo sexual reproduction in order to differentiate the individuals or types involved. [PATO]</p>
</div>

<div id="age-value-(years)" class="field-detail">
<h5><code>age value (years)</code> <em>(required)</em></h5>
<ul>
<li><strong>BICAN UUID:</strong> <code>14eb923a-161d-45e2-889d-81fea7b632b6</code></li>
<li><strong>Data Type:</strong> <code>numeric</code></li>
<li><strong>Aliases:</strong> age_of_death</li>
</ul>
<p>A time quality inhering in a bearer by virtue of how long the bearer has existed. [PATO]</p>
</div>

<div id="year-of-death" class="field-detail">
<h5><code>year of death</code> <em>(required)</em></h5>
<ul>
<li><strong>BICAN UUID:</strong> <code>60445046-d9d8-4f00-959e-9a4c42613e5e</code></li>
<li><strong>Data Type:</strong> <code>date</code></li>
<li><strong>Aliases:</strong> year_of_death</li>
</ul>
<p>The year wherein the subject or donor has ceased to exist.</p>
</div>

<div id="manner-of-death" class="field-detail">
<h5><code>manner of death</code> <em>(required)</em></h5>
<ul>
<li><strong>BICAN UUID:</strong> <code>36eeb35b-5020-4a9e-a74b-6e1104415e0e</code></li>
<li><strong>Data Type:</strong> <code>exclusive_categorical</code></li>
<li><strong>Aliases:</strong> manner_of_death</li>
</ul>
<p>The manner of death is the determination of how the injury or disease leads to death.  There are five manners of death (natural, accident, suicide, homicide, and undetermined).</p>
</div>

<div id="medical-records-available" class="field-detail">
<h5><code>medical records available</code> <em>(required)</em></h5>
<ul>
<li><strong>BICAN UUID:</strong> <code>ee2c9223-f7d1-4c64-a1da-cd7408309955</code></li>
<li><strong>Data Type:</strong> <code>exclusive_categorical</code></li>
<li><strong>Aliases:</strong> medical_records_available</li>
</ul>
<p>The status (available, unavailable) of the medical records of the subject/donor.</p>
</div>

<div id="medical-records-reviewed" class="field-detail">
<h5><code>medical records reviewed</code> <em>(optional)</em></h5>
<ul>
<li><strong>BICAN UUID:</strong> <code>6139b159-c36c-4501-9176-fe2741e3d448</code></li>
<li><strong>Data Type:</strong> <code>exclusive_categorical</code></li>
<li><strong>Aliases:</strong> medical_records_reviewed</li>
</ul>
<p>The status (reviewed, not reviewed) of the medical records of the subject/donor.</p>
</div>

<div id="species" class="field-detail">
<h5><code>species</code> <em>(required)</em></h5>
<ul>
<li><strong>BICAN UUID:</strong> <code>d11fb2ce-bfdb-4735-9b17-b6ba606520b1</code></li>
<li><strong>Data Type:</strong> <code>exclusive_categorical</code></li>
<li><strong>Aliases:</strong> species</li>
</ul>
<p>The species of a subject/donor/sample/specimen.</p>
</div>

<div id="behavioral-scoring-available" class="field-detail">
<h5><code>behavioral scoring available</code> <em>(required)</em></h5>
<ul>
<li><strong>BICAN UUID:</strong> <code>ea33881a-9813-4111-979b-135355e8141e</code></li>
<li><strong>Data Type:</strong> <code>exclusive_categorical</code></li>
<li><strong>Aliases:</strong> behavioral_scoring_available</li>
</ul>
<p>The status (available, unavailable) of the behavioral scoring results for a subject/donor/specimen.</p>
</div>

<div id="behavioral-scoring-type" class="field-detail">
<h5><code>behavioral scoring type</code> <em>(optional)</em></h5>
<ul>
<li><strong>BICAN UUID:</strong> <code>0a7a1eeb-8682-4261-8221-82d587dde0fa</code></li>
<li><strong>Data Type:</strong> <code>text</code></li>
<li><strong>Aliases:</strong> behavioral_scoring_type</li>
</ul>
<p>The type of behavioral scoring that is available for a subject/donor/specimen.</p>
</div>

#### Infectious Disease Testing

<div id="test-name" class="field-detail">
<h5><code>test name</code> <em>(optional)</em></h5>
<ul>
<li><strong>BICAN UUID:</strong> <code>b6865e15-7538-4890-be99-a6f9e9920af3</code></li>
<li><strong>Data Type:</strong> <code>exclusive_categorical</code></li>
<li><strong>Aliases:</strong> test_name</li>
</ul>
<p>The name of the test that has been performed.</p>
</div>

<div id="test-result" class="field-detail">
<h5><code>test result</code> <em>(optional)</em></h5>
<ul>
<li><strong>BICAN UUID:</strong> <code>c14ea006-662c-4666-bfd1-6ff580c403ed</code></li>
<li><strong>Data Type:</strong> <code>exclusive_categorical</code></li>
<li><strong>Aliases:</strong> test_result</li>
</ul>
<p>The result(s) of the test that has been performed.</p>
</div>

<div id="testing-tissue-source" class="field-detail">
<h5><code>testing tissue source</code> <em>(required)</em></h5>
<ul>
<li><strong>BICAN UUID:</strong> <code>42f8e11b-d9a3-48fe-ac1e-cd6f4469de46</code></li>
<li><strong>Data Type:</strong> <code>exclusive_categorical</code></li>
<li><strong>Aliases:</strong> tissue_source</li>
</ul>
<p>The tissue sample location or identifier that is the subject of a test.</p>
</div>

#### Non-Brain Specimen Collected

<div id="non-brain-tissue-available" class="field-detail">
<h5><code>non-brain tissue available</code> <em>(required)</em></h5>
<ul>
<li><strong>BICAN UUID:</strong> <code>3a064c96-a956-4cf3-8b77-056b8e392f99</code></li>
<li><strong>Data Type:</strong> <code>exclusive_categorical</code></li>
<li><strong>Aliases:</strong> non_brain_tissue_available</li>
</ul>
<p>The status (yes, no) of whether non-brain tissue from this organism is available.</p>
</div>

<div id="tissue-type" class="field-detail">
<h5><code>tissue type</code> <em>(required)</em></h5>
<ul>
<li><strong>BICAN UUID:</strong> <code>33ccbc85-ae35-44d6-8bc6-c2fb91116cf7</code></li>
<li><strong>Data Type:</strong> <code>exclusive_categorical</code></li>
<li><strong>Aliases:</strong> tissue_type</li>
</ul>
<p>The type of tissue (non-brain) that is available from this organism.</p>
</div>

<div id="tissue-type-details" class="field-detail">
<h5><code>tissue type details</code> <em>(optional)</em></h5>
<ul>
<li><strong>BICAN UUID:</strong> <code>f551cf87-2c6e-4b92-888d-6310e6a500d8</code></li>
<li><strong>Data Type:</strong> <code>text</code></li>
<li><strong>Aliases:</strong> tissue_type_details</li>
</ul>
<p>The details of the non-brain tissue that is available from this organism.</p>
</div>

<!-- schema-properties-end:patchseq -->
