# BICAN Library Minimal Metadata Schema

Document Status: _Endorsed BICAN Standard_

Version: 1.1.1

Owners: Kimberly Smith; na.hong@yale.edu; Wenjin.J.Zheng@uth.tmc.edu

Contributors: Kimberly Smith; Lydia Ng; Melissa Goldman; Cristina Guinto; Fenna Krienen; Suvvi Nadendla; Michelle Giglio; Chongyuan Luo; Joe Nery; Lei Chang; Lisa Anderson; Nick Fitzgerald; Cat Reeves; Jaime McClintock; Chris Frazar

Reviewer: @patrick-lloyd-ray

License: [CC-BY-4.0](https://creativecommons.org/licenses/by/4.0/)

Date Created: 09-09-2023

## Background

The Brain Research Through Advancing Innovative Neurotechnologies® (BRAIN) Initiative Cell Atlas Network (BICAN) aims to transform our understanding of brain cell types and the precise tools needed to access them, bringing us one step closer to unraveling the complex workings of the human brain.

Building on findings from the BRAIN Initiative Cell Census Network (BICCN), BICAN takes the next step in mapping brain cells and circuits across multiple species, with an emphasis on humans. The aim of BICAN is to generate a complete reference atlas of cell types in the human brain across the lifespan, which can be shared and used throughout the research community. In addition to developing a “parts list” detailing the vast array of neurons and non-neuronal cells in the human brain, the project also aims to map cell interactions that underlie a wide range of brain disorders.

To this end, BICAN aims to support the publication, sharing, and exploration of datasets generated in the course of the project. Creating a complete reference atlas from multiple datasets requires vast harmonization of metadata. In order to facilitate the harmonization of metadata, we require datasets include a small set of metadata available from data submitters.

This document describes a schema, a type of contract, that BICAN requires of all libraries to enable searching, filtering, and integration of datasets.

Note that the requirements in the schema are just the minimum required information. Datasets often have additional metadata, which is preserved in datasets submitted to the data archives.

## Overview

To harmonize gaps among existing library construction processes, the Library Minimal Metadata (LMM) was developed through the consensus of domain experts, including biomedical researchers, experimenters, data analysts, and informaticians. LMM is a metadata standard that aims to facilitate the interoperation and reuse of essential information and enhance the value of library-related resources.

This metadata standard was created through the work of the Library Minimal Metadata Task Force. A version of this metadata standard is available here: https://docs.google.com/spreadsheets/d/11V0aFRnlQFtnTVyuq2TomIgyNPXwC1Fe/edit#gid=1598277230

This document has the following sections:

- [BICAN Library Minimal Metadata Schema](#bican-library-minimal-metadata-schema)
  - [Background](#background)
  - [Overview](#overview)
  - [General Requirements](#general-requirements)
  - [Recieve Sample](#recieve-sample)
  - [Generate Library](#generate-library)
  - [Pool Library](#pool-library)
  - [Delivery Library Pool](#delivery-library-pool)
  - [Appendix](#appendix)
  - [Changelog](#changelog)
    - [Version 1.2.1](#version-121)
    - [Version 1.2](#version-12)
      - [Added](#added)
    - [Version 1.1.1](#version-111)
      - [Changed](#changed)
    - [Version 1.1](#version-11)
      - [Added](#added-1)

## General Requirements



## Recieve Sample

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td>tissue sample label</td>
    </tr>
    <tr>
      <th>Data Type</th>
        <td><code>text</code>
        </td>
    </tr>
    <tr>
      <th>Definition</th>
        <td>Identifier name for final intact piece of tissue before cell or nuclei prep.  This piece of tissue will be used in dissociation and has an ROI associated with it.</td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td>2e4ca2fc-2d77-4d19-af45-d0fb7bbc2269</td>
    </tr>    
</tbody></table>
<br>

## Generate Library

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td>amplified cDNA label</td>
    </tr>
    <tr>
      <th>Data Type</th>
        <td><code>text</code>
        </td>
    </tr>
    <tr>
      <th>Definition</th>
        <td>Name of a collection of cDNA molecules derived and amplified from an input barcoded_cell_sample.  These cDNA molecules represent the gene expression of each cell, with all cDNA molecules from a given cell retaining that cell's unique barcode from the cell barcoding step.  This is a necessary step for GEX methods but is not used for ATAC methods.</td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td>e2606a11-114e-472f-9e05-33f9b6fc3089</td>
    </tr>    
</tbody></table>
<br>

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td>amplified cDNA amplified quantity ng</td>
    </tr>
    <tr>
      <th>Data Type</th>
        <td><code>integer</code>
        </td>
    </tr>
    <tr>
      <th>Definition</th>
        <td>Amount of cDNA produced after cDNA amplification measured in nanograms.</td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td>0db79d05-8612-4896-b9d3-eb1558841449</td>
    </tr>    
</tbody></table>
<br>

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td>amplified cDNA PCR cycles</td>
    </tr>
    <tr>
      <th>Data Type</th>
        <td><code>integer</code>
        </td>
    </tr>
    <tr>
      <th>Definition</th>
        <td>Number of PCR cycles used during cDNA amplification for this cDNA.</td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td>3827634c-3f8f-4760-b358-86ce4b030238</td>
    </tr>    
</tbody></table>
<br>

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td>cDNA amplification process date</td>
    </tr>
    <tr>
      <th>Data Type</th>
        <td><code>date</code>
        </td>
    </tr>
    <tr>
      <th>Definition</th>
        <td>Date of cDNA amplification.</td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td>6cc333e7-9b98-497f-b7b1-eae904db2400</td>
    </tr>    
</tbody></table>
<br>

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td>amplified cDNA RNA amplification pass-fail</td>
    </tr>
    <tr>
      <th>Data Type</th>
        <td><code>enum</code>
        </td>
    </tr>
    <tr>
      <th>Definition</th>
        <td>Pass or Fail result based on qualitative assessment of cDNA yield and size.</td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td>bc62bdb2-7dc8-4404-bb84-ce0bbcae59e5</td>
    </tr>    
</tbody></table>
<br>

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td>amplified cDNA percent cDNA longer than 400bp</td>
    </tr>
    <tr>
      <th>Data Type</th>
        <td><code>integer</code>
        </td>
    </tr>
    <tr>
      <th>Definition</th>
        <td>QC metric to measure mRNA degradation of cDNA.  Higher % is higher quality starting material.  Over 400bp is used as a universal cutoff for intact (full length) vs degraded cDNA and is a common output from Bioanalyzer and Fragment Analyzer elecropheragrams.</td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td>8d150467-f69e-461c-b54c-bcfd22f581e5</td>
    </tr>    
</tbody></table>
<br>

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td>cDNA amplification set</td>
    </tr>
    <tr>
      <th>Data Type</th>
        <td><code>text</code>
        </td>
    </tr>
    <tr>
      <th>Definition</th>
        <td>cDNA amplification set, containing multiple amplified_cDNA_names that were processed at the same time.</td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td>42e98a88-50b3-4ea2-871b-2142f6a0dfdd</td>
    </tr>    
</tbody></table>
<br>

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td>barcoded cell sample port well</td>
    </tr>
    <tr>
      <th>Data Type</th>
        <td><code>text</code>
        </td>
    </tr>
    <tr>
      <th>Definition</th>
        <td>Specific position of the loaded port of the 10x chip.  An Enriched or Dissociated Cell Sample is loaded into a port on a chip (creating a Barcoded Cell Sample).  Can be left null for non-10x methods.</td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td>aca38100-d245-4be4-9be3-ba27192779fe</td>
    </tr>    
</tbody></table>
<br>

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td>barcoded cell input quantity count</td>
    </tr>
    <tr>
      <th>Data Type</th>
        <td><code>integer</code>
        </td>
    </tr>
    <tr>
      <th>Definition</th>
        <td>Number of enriched or dissociated cells/nuclei going into the barcoding process.</td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td>aa534269-7c9b-4b63-b990-eea8cda56d0e</td>
    </tr>    
</tbody></table>
<br>

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td>barcoded cell sample label</td>
    </tr>
    <tr>
      <th>Data Type</th>
        <td><code>text</code>
        </td>
    </tr>
    <tr>
      <th>Definition</th>
        <td>Name of a collection of barcoded cells.  Input will be either dissociated_cell_sample or enriched_cell_sample.  Cell barcodes are only guaranteed to be unique within this one collection. One dissociated_cell_sample or enriched_cell_sample can lead to multiple barcoded_cell_samples.</td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td>4c0e6380-e53f-4173-a474-d41e836fefe3</td>
    </tr>    
</tbody></table>
<br>
	
<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td>Expected cell capture</td>
    </tr>
    <tr>
      <th>Data Type</th>
        <td><code>integer</code>
        </td>
    </tr>
    <tr>
      <th>Definition</th>
        <td>Expected number of cells/nuclei of a barcoded_cell_sample that will be barcoded and available for sequencing.  This is a derived number from 'Barcoded cell input quantity count' that is dependent on the "capture rate" of the barcoding method.  It is usually a calculated fraction of the 'Barcoded cell input quantity count' going into the barcoding method.</td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td>f10e928d-5a2b-4943-af18-d8fe5d05528d</td>
    </tr>    
</tbody></table>
<br>

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td>study sets</td>
    </tr>
    <tr>
      <th>Data Type</th>
        <td><code>text</code>
        </td>
    </tr>
    <tr>
      <th>Definition</th>
        <td>Intended cohort or dataset that the Barcoded Cell Sample initially belongs to.  This Study helps to group together samples that are meant to be analyzed together.  Multiple Studies can be assigned to a Barcoded Cell Sample.  These studies are more granular than the grant or PI and can be used to group together samples from related ROIs.</td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td>8877f8f0-3939-4062-84c9-414bdcdd04ca</td>
    </tr>    
</tbody></table>
<br>

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td>1st round barcodes</td>
    </tr>
    <tr>
      <th>Data Type</th>
        <td><code>text</code>
        </td>
    </tr>
    <tr>
      <th>Definition</th>
        <td>Specific element for Paired-tag.</td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td>24bc6d6b-fd91-4c7f-9357-22664b3e0632</td>
    </tr>    
</tbody></table>
<br>

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td>2nd&3rd round barcode</td>
    </tr>
    <tr>
      <th>Data Type</th>
        <td><code>text</code>
        </td>
    </tr>
    <tr>
      <th>Definition</th>
        <td>Specific element for Paired-tag.</td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td>95c7fe57-2eae-42ce-b4a2-6445574e8e92</td>
    </tr>    
</tbody></table>
<br>

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td>Antibody information</td>
    </tr>
    <tr>
      <th>Data Type</th>
        <td><code>text</code>
        </td>
    </tr>
    <tr>
      <th>Definition</th>
        <td>Vendor, Catalog# and Lot#</td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td>a7af711c-f30b-469b-a3ca-b78b1b2fb99a</td>
    </tr>    
</tbody></table>
<br>
	
<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td>dissociated cell sample cell prep type</td>
    </tr>
    <tr>
      <th>Data Type</th>
        <td><code>enum</code>
        </td>
    </tr>
    <tr>
      <th>Definition</th>
        <td>The type of cell preparation. For example: Cells, Nuclei. This is a property of dissociated_cell_sample.</td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td>baae4ac3-f959-4594-b943-3a82ec19bd34</td>
    </tr>    
</tbody></table>
<br>

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td>dissociated cell sample label</td>
    </tr>
    <tr>
      <th>Data Type</th>
        <td><code>text</code>
        </td>
    </tr>
    <tr>
      <th>Definition</th>
        <td>Name of a collection of dissociated cells or nuclei derived from dissociation of a tissue sample.</td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td>65e2c7da-9eb4-45b2-8ccb-d69ef9785ee2</td>
    </tr>    
</tbody></table>
<br>
	
<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td>dissociated cell source barcode name</td>
    </tr>
    <tr>
      <th>Data Type</th>
        <td><code>text</code>
        </td>
    </tr>
    <tr>
      <th>Definition</th>
        <td>Name of oligo used in cell plexing.  The oligo will tag allow separate dissociated cell samples to be combined downstream in the barcoded cell sample.  The oligo name is associated with a sequence in a lookup table.  This sequence will be needed to during analysis, after alignment, to associate reads with parent dissociated cell sample.</td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td>184abbaf-baff-4b5f-b51e-dd38de6006af</td>
    </tr>    
</tbody></table>
<br>

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td>dissociated cell source barcode name</td>
    </tr>
    <tr>
      <th>Data Type</th>
        <td><code>ValueSet</code>
        </td>
    </tr>
    <tr>
      <th>Definition</th>
        <td>Name of oligo used in cell plexing.  The oligo will tag allow separate dissociated cell samples to be combined downstream in the barcoded cell sample.  The oligo name is associated with a sequence in a lookup table.  This sequence will be needed to during analysis, after alignment, to associate reads with parent dissociated cell sample.</td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td>0c8628d0-809b-458c-b4b3-686131dceef8</td>
    </tr>    
</tbody></table>
<br>

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td>dissociated cell sample preparation date</td>
    </tr>
    <tr>
      <th>Data Type</th>
        <td><code>Date</code>
        </td>
    </tr>
    <tr>
      <th>Definition</th>
        <td>Date of dissociated cell sample creation.</td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td>c508b63d-a1b4-42de-9b22-9c4736deac6e</td>
    </tr>    
</tbody></table>
<br>

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td>patched cell structure</td>
    </tr>
    <tr>
      <th>Data Type</th>
        <td><code>Value Set</code>
        </td>
    </tr>
    <tr>
      <th>Definition</th>
        <td>Ontological structure assigned to a single patched cell.  This is typically assigned and confirmed after imaging.</td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td>7636b4c8-12f6-4b33-bdc6-c2f1a3b1c953</td>
    </tr>    
</tbody></table>
<br>

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td>Enriched cell sample container name</td>
    </tr>
    <tr>
      <th>Data Type</th>
        <td><code>text</code>
        </td>
    </tr>
    <tr>
      <th>Definition</th>
        <td>Name of container (strip or tube or plate) of the enriched_cell_prep.  This container could contain 1 or more enriched_cell_samples.</td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td>5ace37aa-85d6-4493-909e-8fc221ec2609</td>
    </tr>    
</tbody></table>
<br>

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td>Enriched cell sample name</td>
    </tr>
    <tr>
      <th>Data Type</th>
        <td><code>text</code>
        </td>
    </tr>
    <tr>
      <th>Definition</th>
        <td>Name of collection of enriched cells or nuclei after enrichment process (usually via FACS using the Enrichment Plan) applied to dissociated_cell_sample.</td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td>bb3fc701-23a7-45c1-890d-7471730e0ec1</td>
    </tr>    
</tbody></table>
<br>

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td>enrichment population</td>
    </tr>
    <tr>
      <th>Data Type</th>
        <td><code>text</code>
        </td>
    </tr>
    <tr>
      <th>Definition</th>
        <td>Actual percentage of cells as a result of using set of fluorescent marker label(s) to enrich dissociated_cell_sample with desired mix of cell populations.  This plan can also be used to describe 'No FACS' where no enrichment was performed.  This is a property of enriched_cell_prep_container. </td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td>875f1c70-f5aa-45e3-94b9-5e482f6c4830</td>
    </tr>    
</tbody></table>
<br>

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td>enriched cell source barcode name</td>
    </tr>
    <tr>
      <th>Data Type</th>
        <td><code>ValueSet</code>
        </td>
    </tr>
    <tr>
      <th>Definition</th>
        <td>Name of molecular barcode used to individual Enriched Cell Source to allow for pooling of Enriched Cell Sources before 10x load (Barcoding Cell step) [aka 1st round barcodes].</td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td>bdd5e2bf-c6fa-43e6-a5ac-6878fcf814d6</td>
    </tr>    
</tbody></table>
<br>

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td>enriched cell sample preparation date</td>
    </tr>
    <tr>
      <th>Data Type</th>
        <td><code>Date</code>
        </td>
    </tr>
    <tr>
      <th>Definition</th>
        <td>Date of enriched cell sample creation.</td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td>e2fd2d84-3999-4cc4-8f41-e0e2a708f407</td>
    </tr>    
</tbody></table>
<br>

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td>histone modification marker</td>
    </tr>
    <tr>
      <th>Data Type</th>
        <td><code>Text</code>
        </td>
    </tr>
    <tr>
      <th>Definition</th>
        <td>Histone modification marker antibodies (eg H3K27ac, H3K27me3, H3K9me3) used in conjunction with an Enriched Cell Source Barcode in order to combine multiple Enriched Cell Populations before Barcoded Cell Sample step for 10xMultiome method.  Each of the Histone antibodies captures an essential part of the epigenome.</td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td>a2ef2228-e438-4260-95e5-22eb3b35b5a9</td>
    </tr>    
</tbody></table>
<br>

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td>library avg size bp</td>
    </tr>
    <tr>
      <th>Data Type</th>
        <td><code>integer</code>
        </td>
    </tr>
    <tr>
      <th>Definition</th>
        <td>Average size of the library in terms of base pairs.  This is used to calculate the molarity before pooling and sequencing.</td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td>f851eba9-56d1-4472-9d0c-d7f8bc33000a</td>
    </tr>    
</tbody></table>
<br>

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td>library method</td>
    </tr>
    <tr>
      <th>Data Type</th>
        <td><code>enum</code>
        </td>
    </tr>
    <tr>
      <th>Definition</th>
        <td>Standardized nomenclature to describe the library method used.  This specifies the alignment method required for the library.  For example, 10xV3.1 (for RNASeq single assay), 10xMult-GEX (for RNASeq multiome assay), and 10xMult-ATAC (for ATACSeq multiome assay).</td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td>7b60d59e-fdd7-4b27-a2d4-cae9b69103a6</td>
    </tr>    
</tbody></table>
<br>

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td>Library concentration nm</td>
    </tr>
    <tr>
      <th>Data Type</th>
        <td><code>integer</code>
        </td>
    </tr>
    <tr>
      <th>Definition</th>
        <td>Concentration of library in terms of nM (nMol/L).  Number of molecules is needed for accurate pooling of the libraries and for generating the number of target reads/cell in sequencing.</td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td>90805b3f-f380-4f23-b159-e7eaa0c8f052</td>
    </tr>    
</tbody></table>
<br>

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td>library creation date</td>
    </tr>
    <tr>
      <th>Data Type</th>
        <td><code>date</code>
        </td>
    </tr>
    <tr>
      <th>Definition</th>
        <td>Date of library construction.</td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td>9c2f575d-1b64-451d-894f-656861afe07a</td>
    </tr>    
</tbody></table>
<br>

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td>library input ng</td>
    </tr>
    <tr>
      <th>Data Type</th>
        <td><code>integer</code>
        </td>
    </tr>
    <tr>
      <th>Definition</th>
        <td>Amount of cDNA going into library construction in nanograms.</td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td>e4d31d97-722d-4771-a0e4-e6062190f2c1</td>
    </tr>    
</tbody></table>
<br>
	
<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td>library label</td>
    </tr>
    <tr>
      <th>Data Type</th>
        <td><code>text</code>
        </td>
    </tr>
    <tr>
      <th>Definition</th>
        <td>Name of a library, which is a collection of fragmented and barcode-indexed DNA molecules for sequencing.  An index or barcode is typically introduced to enable identification of library origin to allow libraries to be pooled together for sequencing.</td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td>f717e254-3630-4342-be7b-4d56376e7afe</td>
    </tr>    
</tbody></table>
<br>

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td>library prep pass-fail</td>
    </tr>
    <tr>
      <th>Data Type</th>
        <td><code>enum</code>
        </td>
    </tr>
    <tr>
      <th>Definition</th>
        <td>Pass or Fail result based on qualitative assessment of library yield and size.</td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td>6817ede2-7ead-402d-9dbc-131aca627c6c</td>
    </tr>    
</tbody></table>
<br>

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td>library prep set</td>
    </tr>
    <tr>
      <th>Data Type</th>
        <td><code>text</code>
        </td>
    </tr>
    <tr>
      <th>Definition</th>
        <td>Library set, containing multiple library_names that were processed at the same time.</td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td>b124ffa9-9134-4a61-a30d-bb191b2fc7fa</td>
    </tr>    
</tbody></table>
<br>

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td>library quantification fmol</td>
    </tr>
    <tr>
      <th>Data Type</th>
        <td><code>integer</code>
        </td>
    </tr>
    <tr>
      <th>Definition</th>
        <td>Amount of library generated in terms of femtomoles.</td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td>4c09ada7-c116-48bc-8fb1-0dcf5c4b939a</td>
    </tr>    
</tbody></table>
<br>

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td>library quantification ng</td>
    </tr>
    <tr>
      <th>Data Type</th>
        <td><code>integer</code>
        </td>
    </tr>
    <tr>
      <th>Definition</th>
        <td>Amount of library generated in terms of nanograms.</td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td>318b2d3a-dae7-4c63-bfbb-93862b92f63e</td>
    </tr>    
</tbody></table>
<br>

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td>R1/R2 index name</td>
    </tr>
    <tr>
      <th>Data Type</th>
        <td><code>text</code>
        </td>
    </tr>
    <tr>
      <th>Definition</th>
        <td>Name of the pair of library indexes used for sequencing.  Indexes allow libraries to be pooled together for sequencing.  Sequencing output (fastq) are demultiplexed by using the indexes for each library.  The name will be associated with the sequences of i7, i5, and i5as, which are needed by SeqCores for demultiplexing.  The required direction of the sequence (sense or antisense) of the index can differ depending on sequencing instruments.</td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td>c94b5d8a-e92d-47af-8c0e-ea3b58be4d06</td>
    </tr>    
</tbody></table>
<br>


## Pool Library

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td>library aliquot label</td>
    </tr>
    <tr>
      <th>Data Type</th>
        <td><code>text</code>
        </td>
    </tr>
    <tr>
      <th>Definition</th>
        <td>One library in the library pool.  Each Library_aliquot_name in a library pool will have a unique R1/R2 index to allow for sequencing together then separating the sequencing output by originating library aliquot through the process of demultiplexing.  The resulting demultiplexed fastq files will include the library_aliquot_name.</td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td>34191bad-d167-4335-8224-ade897d3728e</td>
    </tr>    
</tbody></table>
<br>

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td>fastq file alignment status</td>
    </tr>
    <tr>
      <th>Data Type</th>
        <td><code>Categorical Variable</code>
        </td>
    </tr>
    <tr>
      <th>Definition</th>
        <td>The QC status of the fastq file alignment process result.</td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td>834a0e66-fd81-4d9c-b379-146372c3a629</td>
    </tr>    
</tbody></table>
<br>

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td>library pool tube internal label</td>
    </tr>
    <tr>
      <th>Data Type</th>
        <td><code>text</code>
        </td>
    </tr>
    <tr>
      <th>Definition</th>
        <td>Library Pool Tube local name.  Label of the tube containing the library pool, which is made up of multiple library_aliquots.  This is a Library Lab local tube name, before the pool is aliquoted to the Seq Core provided tube 'Library Pool Tube Name'.</td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td>f1fdea98-7849-4def-a62f-a04cbbf98922</td>
    </tr>    
</tbody></table>
<br>

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td>embargo date</td>
    </tr>
    <tr>
      <th>Data Type</th>
        <td><code>date</code>
        </td>
    </tr>
    <tr>
      <th>Definition</th>
        <td>date until which data much be embargoed.</td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td>e7bc38d8-7315-40be-b8b7-923bf770ff38</td>
    </tr>    
</tbody></table>
<br>

## Delivery Library Pool

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td>SeqCore library pool tube barcode</td>
    </tr>
    <tr>
      <th>Data Type</th>
        <td><code>text</code>
        </td>
    </tr>
    <tr>
      <th>Definition</th>
        <td>Library Pool tube name as provided by the SeqCore (often a barcode).  This tube is provided from the SeqCore and is part of the SeqCore tracking system.</td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td>da02a0ee-9abf-45ef-abb1-981f1aaba6b2</td>
    </tr>    
</tbody></table>
<br>

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td>library pool label</td>
    </tr>
    <tr>
      <th>Data Type</th>
        <td><code>text</code>
        </td>
    </tr>
    <tr>
      <th>Definition</th>
        <td>Library lab's library pool name.  For some labs this may be the same as "Libray pool tube local name".   Other labs distinguish between the local tube label of the library pool and the library pool name provided to SeqCore for tracking.  Local Pool Name is used to communicate sequencing status between SeqCore and Library Labs.</td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td>29e0578b-6427-4c93-b29b-bde27fbadeec</td>
    </tr>    
</tbody></table>
<br>
	
<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td>library pool tube avg size bp</td>
    </tr>
    <tr>
      <th>Data Type</th>
        <td><code>integer</code>
        </td>
    </tr>
    <tr>
      <th>Definition</th>
        <td>Average insert size of library pool, measured in base pairs.</td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td>cf1b7c96-cdc1-4eed-8e76-ac44fbd151f7</td>
    </tr>    
</tbody></table>
<br>

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td>library pool fmol</td>
    </tr>
    <tr>
      <th>Data Type</th>
        <td><code>integer</code>
        </td>
    </tr>
    <tr>
      <th>Definition</th>
        <td>Amount of library pool in the tube as measured in femtamoles (fmol).</td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td>af1a6f3f-aca9-4452-b86e-f3c70c3600b6</td>
    </tr>    
</tbody></table>
<br>
	
<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td>loading concentration pM</td>
    </tr>
    <tr>
      <th>Data Type</th>
        <td><code>float</code>
        </td>
    </tr>
    <tr>
      <th>Definition</th>
        <td>Sequencer Loading Concentration as measured in pM (pmol/L).  This is a value used by the SeqCore.</td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td>a1a1b046-549d-4e94-9b3c-5fac2a31fdd6</td>
    </tr>    
</tbody></table>
<br>

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td>Length of Read 2 (for Paired End Runs)</td>
    </tr>
    <tr>
      <th>Data Type</th>
        <td><code>integer</code>
        </td>
    </tr>
    <tr>
      <th>Definition</th>
        <td>Separate field to replace the combined field "Sequencing cycle". Sequencing Cycle is needed for sequencing the library pool.  The sequencing cycle needed is specific to the Library Chemistry Method and is required instruction to the SeqCores.</td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td>0b9a9cbc-b8dd-42a2-a567-aafd9370db30</td>
    </tr>    
</tbody></table>
<br>

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td>Length of Index 1 (i7 Primer)</td>
    </tr>
    <tr>
      <th>Data Type</th>
        <td><code>integer</code>
        </td>
    </tr>
    <tr>
      <th>Definition</th>
        <td>Separate field to replace the combined field "Sequencing cycle". Sequencing Cycle is needed for sequencing the library pool.  The sequencing cycle needed is specific to the Library Chemistry Method and is required instruction to the SeqCores.</td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td>0b94df0d-d96e-4d49-a498-b3eb83afc5f8</td>
    </tr>    
</tbody></table>
<br>
 	
<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td>Length of Index 2 (i5 Primer)</td>
    </tr>
    <tr>
      <th>Data Type</th>
        <td><code>integer</code>
        </td>
    </tr>
    <tr>
      <th>Definition</th>
        <td>Separate field to replace the combined field "Sequencing cycle". Sequencing Cycle is needed for sequencing the library pool.  The sequencing cycle needed is specific to the Library Chemistry Method and is required instruction to the SeqCores.</td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td>a61c1d55-b880-499c-ba4a-30311fdca62f</td>
    </tr>    
</tbody></table>
<br>

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td>Length of Read 1</td>
    </tr>
    <tr>
      <th>Data Type</th>
        <td><code>integer</code>
        </td>
    </tr>
    <tr>
      <th>Definition</th>
        <td>Separate field to replace the combined field "Sequencing cycle". Sequencing Cycle is needed for sequencing the library pool.  The sequencing cycle needed is specific to the Library Chemistry Method and is required instruction to the SeqCores.</td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td>f22ac08a-bb81-4524-91f0-0e1e1a032335</td>
    </tr>    
</tbody></table>
<br>

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td>library pool tube contents nM</td>
    </tr>
    <tr>
      <th>Data Type</th>
        <td><code>float</code>
        </td>
    </tr>
    <tr>
      <th>Definition</th>
        <td>Library pool concentration as measured in nanomolarity (nMol/L).</td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td>32f2d02b-7300-4554-aa93-6de6e456eda7</td>
    </tr>    
</tbody></table>
<br>

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td>library pool tube volume ul</td>
    </tr>
    <tr>
      <th>Data Type</th>
        <td><code>integer</code>
        </td>
    </tr>
    <tr>
      <th>Definition</th>
        <td>Library pool volume as measured in ul.</td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td>b1b923ac-c218-4db4-a3b1-45a219612567</td>
    </tr>    
</tbody></table>
<br>
	
<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td>PhiX spike in percent</td>
    </tr>
    <tr>
      <th>Data Type</th>
        <td><code>integer</code>
        </td>
    </tr>
    <tr>
      <th>Definition</th>
        <td>PhiX spike-in percent desired to be added to the library pool for sequencing.  PhiX is used to increase complexity of the sample being sequenced, to reduce sequencing artifacts maintain sequencing quality on the instruments.  This is an optional instruction to the SeqCore.</td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td>b5ab26ad-d523-406e-a85b-e77f2f4b06b5</td>
    </tr>    
</tbody></table>
<br>

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td>custom primers</td>
    </tr>
    <tr>
      <th>Data Type</th>
        <td><code>boolean</code>
        </td>
    </tr>
    <tr>
      <th>Definition</th>
        <td>Custom sequencing primers if needed, indicate with reads require them (R1/R2/i7/i5).</td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td>76c905d5-ef4a-421a-bd59-b541c5c1d45d</td>
    </tr>    
</tbody></table>
<br>

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td>library pool construction date</td>
    </tr>
    <tr>
      <th>Data Type</th>
        <td><code>Date</code>
        </td>
    </tr>
    <tr>
      <th>Definition</th>
        <td>Date of library construction.</td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td>ef950ca1-2a62-4fce-a826-6c27d94d3be3</td>
    </tr>    
</tbody></table>
<br>

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td>flowcell</td>
    </tr>
    <tr>
      <th>Data Type</th>
        <td><code>text</code>
        </td>
    </tr>
    <tr>
      <th>Definition</th>
        <td></td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td>4c8d7ac8-d3e3-4177-a93d-18ec2302c392</td>
    </tr>    
</tbody></table>
<br>


## Appendix

<!-- schema-properties-start -->
## Schema properties
*Auto-generated from CSV. Do not edit this section manually.*

**Related LinkML model:** [Library Generation Model](https://brain-bican.github.io/models/index_library_generation/)

### Properties

#### amplified cdna

| Property | Type | Required | Aliases | Description |
|----------|------|----------|---------|-------------|
| [`amplified cDNA label`](#amplified-cdna-label) | Text | no | amplified cdna name | Name of a collection of cDNA molecules derived and amplified from an input barcoded_cell_sample.  These cDNA molecules r… |
| [`amplified cDNA amplified quantity ng`](#amplified-cdna-amplified-quantity-ng) | Float | no | amplified quantity ng | Amount of cDNA produced after cDNA amplification measured in nanograms |
| [`amplified cDNA PCR cycles`](#amplified-cdna-pcr-cycles) | Integer | no | cDNA amplification cycles | Number of PCR cycles used during cDNA amplification for this cDNA. |
| [`cDNA amplification process date`](#cdna-amplification-process-date) | Date | no | cDNA amplification date | Date of cDNA amplification. |
| [`amplified cDNA RNA amplification pass-fail`](#amplified-cdna-rna-amplification-pass-fail) | ValueSet | no | cDNA amplification pass-fail result | Pass or Fail result based on qualitative assessment of cDNA yield and size. |
| [`amplified cDNA percent cDNA longer than 400bp`](#amplified-cdna-percent-cdna-longer-than-400bp) | Float | no | cDNA amplification percent cDNA greater than 400bp | QC metric to measure mRNA degradation of cDNA.  Higher % is higher quality starting material.  Over 400bp is used as a u… |
| [`cDNA amplification set`](#cdna-amplification-set) | Text | no | — | cDNA amplification set, containing multiple amplified_cDNA_names that were processed at the same time. |

#### barcoded cell sample

| Property | Type | Required | Aliases | Description |
|----------|------|----------|---------|-------------|
| [`barcoded cell sample port well`](#barcoded-cell-sample-port-well) | Text | no | 10x chip port well | Specific position of the loaded port of the 10x chip.  An Enriched or Dissociated Cell Sample is loaded into a port on a… |
| [`barcoded cell input quantity count`](#barcoded-cell-input-quantity-count) | Integer | no | — | Number of enriched or dissociated cells/nuclei going into the barcoding process. |
| [`barcoded cell sample label`](#barcoded-cell-sample-label) | Text | yes | barcoded cell sample name | Name of a collection of barcoded cells.  Input will be either dissociated_cell_sample or enriched_cell_sample.  Cell bar… |
| [`expected cell capture`](#expected-cell-capture) | Integer | no | — | Expected number of cells/nuclei of a barcoded_cell_sample that will be barcoded and available for sequencing.  This is a… |
| [`study sets`](#study-sets) | Text | no | — | Intended cohort or dataset that the Barcoded Cell Sample initially belongs to.  This Study helps to group together sampl… |

#### dissociated cell sample

| Property | Type | Required | Aliases | Description |
|----------|------|----------|---------|-------------|
| [`dissociated cell sample cell prep type`](#dissociated-cell-sample-cell-prep-type) | ValueSet | yes | cell prep type | The type of cell preparation. For example: Cells, Nuclei. This is a property of dissociated_cell_sample. |
| [`dissociated cell sample label`](#dissociated-cell-sample-label) | Text | no | dissociated cell sample name | Name of a collection of dissociated cells or nuclei derived from dissociation of a tissue sample. |
| [`dissociated cell source barcode name`](#dissociated-cell-source-barcode-name) | Text | no | — | Name of oligo used in cell plexing.  The oligo will tag allow separate dissociated cell samples to be combined downstrea… |
| [`dissociated cell source barcode name`](#dissociated-cell-source-barcode-name) | ValueSet | no | — | Name of oligo used in cell plexing. The oligo will tag allow separate dissociated cell samples to be combined downstream… |
| [`dissociated cell sample preparation date`](#dissociated-cell-sample-preparation-date) | Date | no | — | Date of dissociated cell sample creation. |
| [`patched cell structure`](#patched-cell-structure) | ValueSet | no | — | Ontological structure assigned to a single patched cell. This is typically assigned and confirmed after imaging. |

#### enriched cell sample

| Property | Type | Required | Aliases | Description |
|----------|------|----------|---------|-------------|
| [`enriched cell sample container name`](#enriched-cell-sample-container-name) | Text | no | — | Name of container (strip or tube or plate) of the enriched_cell_prep.  This container could contain 1 or more enriched_c… |
| [`enriched cell sample name`](#enriched-cell-sample-name) | Text | no | — | Name of collection of enriched cells or nuclei after enrichment process (usually via FACS using the Enrichment Plan) app… |
| [`enrichment population`](#enrichment-population) | Text | no | — | Actual percentage of cells as a result of using set of fluorescent marker label(s) to enrich dissociated_cell_sample wit… |
| [`enriched cell source barcode name`](#enriched-cell-source-barcode-name) | ValueSet | no | — | Name of molecular barcode used to individual Enriched Cell Source to allow for pooling of Enriched Cell Sources before 1… |
| [`enriched cell sample preparation date`](#enriched-cell-sample-preparation-date) | Date | no | — | Date of enriched cell sample creation. |
| [`histone modification marker`](#histone-modification-marker) | Text | no | — | Histone modification marker antibodies (eg H3K27ac, H3K27me3, H3K9me3) used in conjunction with an Enriched Cell Source … |

#### library

| Property | Type | Required | Aliases | Description |
|----------|------|----------|---------|-------------|
| [`library avg size bp`](#library-avg-size-bp) | Integer | no | — | Average size of the library in terms of base pairs.  This is used to calculate the molarity before pooling and sequencin… |
| [`library method`](#library-method) | ValueSet | yes | library chemistry method | Standardized nomenclature to describe the library method used.  This specifies the alignment method required for the lib… |
| [`library concentration nm`](#library-concentration-nm) | Float | no | — | Concentration of library in terms of nM (nMol/L).  Number of molecules is needed for accurate pooling of the libraries a… |
| [`library creation date`](#library-creation-date) | Date | no | library construction date | Date of library construction |
| [`library input ng`](#library-input-ng) | Integer | no | — | Amount of cDNA going into library construction in nanograms. |
| [`library label`](#library-label) | Text | no | library name | Name of a library, which is a collection of fragmented and barcode-indexed DNA molecules for sequencing.  An index or ba… |
| [`library prep pass-fail`](#library-prep-pass-fail) | ValueSet | no | library prep pass-fail result | Pass or Fail result based on qualitative assessment of library yield and size. |
| [`library prep set`](#library-prep-set) | Text | no | — | Library set, containing multiple library_names that were processed at the same time. |
| [`library quantification fmol`](#library-quantification-fmol) | Integer | no | — | Amount of library generated in terms of femtomoles |
| [`library quantification ng`](#library-quantification-ng) | Integer | no | — | Amount of library generated in terms of nanograms |
| [`R1/R2 index name`](#r1/r2-index-name) | Text | yes | — | Name of the pair of library indexes used for sequencing.  Indexes allow libraries to be pooled together for sequencing. … |

#### library aliquot

| Property | Type | Required | Aliases | Description |
|----------|------|----------|---------|-------------|
| [`library aliquot label`](#library-aliquot-label) | Text | yes | library aliquot name | One library in the library pool.  Each Library_aliquot_name in a library pool will have a unique R1/R2 index to allow fo… |
| [`fastq file alignment status`](#fastq-file-alignment-status) | ValueSet | yes | library aliquot QC result | The QC status of the fastq file alignment process result. |

#### library pool

| Property | Type | Required | Aliases | Description |
|----------|------|----------|---------|-------------|
| [`library pool tube internal label`](#library-pool-tube-internal-label) | Text | yes | libray pool tube local name | Library Pool Tube local name.  Label of the tube containing the library pool, which is made up of multiple library_aliqu… |
| [`embargo date`](#embargo-date) | Text | no | — | date until which data much be embargoed |
| [`SeqCore library pool tube barcode`](#seqcore-library-pool-tube-barcode) | Text | yes | — | Library Pool tube name as provided by the SeqCore (often a barcode).  This tube is provided from the SeqCore and is part… |
| [`library pool label`](#library-pool-label) | Text | yes | local pool name | Library lab&#x27;s library pool name.  For some labs this may be the same as &quot;Libray pool tube local name&quot;.   Other labs dist… |
| [`library pool tube avg size bp`](#library-pool-tube-avg-size-bp) | Integer | no | library pool avg size bp | Average insert size of library pool, measured in base pairs. |
| [`library pool fmol`](#library-pool-fmol) | Float | no | — | Amount of library pool in the tube as measured in femtamoles (fmol) |
| [`loading concentration pM`](#loading-concentration-pm) | Float | no | — | Sequencer Loading Concentration as measured in pM (pmol/L).  This is a value used by the SeqCore. |
| [`length of Read 2 (for Paired End Runs)`](#length-of-read-2-(for-paired-end-runs)) | Integer | yes | — | Separate field to replace the combined field &quot;Sequencing cycle&quot;. Sequencing Cycle is needed for sequencing the library p… |
| [`length of Index 1 (i7 Primer)`](#length-of-index-1-(i7-primer)) | Integer | yes | — | Separate field to replace the combined field &quot;Sequencing cycle&quot;. Sequencing Cycle is needed for sequencing the library p… |
| [`length of Index 2 (i5 Primer)`](#length-of-index-2-(i5-primer)) | Integer | yes | — | Separate field to replace the combined field &quot;Sequencing cycle&quot;. Sequencing Cycle is needed for sequencing the library p… |
| [`length of Read 1`](#length-of-read-1) | Integer | yes | — | Separate field to replace the combined field &quot;Sequencing cycle&quot;. Sequencing Cycleis  needed for sequencing the library p… |
| [`library pool tube contents nM`](#library-pool-tube-contents-nm) | Float | no | library pool concentration (nM) | Library pool concentration as measured in nanomolarity (nMol/L) |
| [`library pool tube volume ul`](#library-pool-tube-volume-ul) | Integer | no | — | Library pool volume as measured in ul |
| [`PhiX spike in percent`](#phix-spike-in-percent) | Float | no | — | PhiX spike-in percent desired to be added to the library pool for sequencing.  PhiX is used to increase complexity of th… |
| [`custom primers`](#custom-primers) | Boolean | no | — | Custom sequencing primers if needed, indicate with reads require them (R1/R2/i7/i5) |
| [`library pool construction date`](#library-pool-construction-date) | Date | no | — | Date of library pool construction. |
| [`flowcell`](#flowcell) | Text | no | — |  |

#### tissue sample

| Property | Type | Required | Aliases | Description |
|----------|------|----------|---------|-------------|
| [`tissue sample label`](#tissue-sample-label) | text | yes | tissue name\|tissue sample label | Identifier name for final intact piece of tissue before cell or nuclei prep.  This piece of tissue will be used in disso… |

### Property Details

#### amplified cdna

<div id="amplified-cdna-label" class="field-detail">
<h5><code>amplified cDNA label</code> <em>(optional)</em></h5>
<ul>
<li><strong>BICAN UUID:</strong> <code>e2606a11-114e-472f-9e05-33f9b6fc3089</code></li>
<li><strong>Data Type:</strong> <code>Text</code></li>
<li><strong>Aliases:</strong> amplified cdna name</li>
<li><strong>Subsets:</strong> analysis</li>
</ul>
<p>Name of a collection of cDNA molecules derived and amplified from an input barcoded_cell_sample.  These cDNA molecules represent the gene expression of each cell, with all cDNA molecules from a given cell retaining that cell&#x27;s unique barcode from the cell barcoding step.  This is a necessary step for GEX methods but is not used for ATAC methods.</p>
</div>

<div id="amplified-cdna-amplified-quantity-ng" class="field-detail">
<h5><code>amplified cDNA amplified quantity ng</code> <em>(optional)</em></h5>
<ul>
<li><strong>BICAN UUID:</strong> <code>0db79d05-8612-4896-b9d3-eb1558841449</code></li>
<li><strong>Data Type:</strong> <code>Float</code></li>
<li><strong>Aliases:</strong> amplified quantity ng</li>
<li><strong>Subsets:</strong> analysis</li>
</ul>
<p>Amount of cDNA produced after cDNA amplification measured in nanograms</p>
</div>

<div id="amplified-cdna-pcr-cycles" class="field-detail">
<h5><code>amplified cDNA PCR cycles</code> <em>(optional)</em></h5>
<ul>
<li><strong>BICAN UUID:</strong> <code>3827634c-3f8f-4760-b358-86ce4b030238</code></li>
<li><strong>Data Type:</strong> <code>Integer</code></li>
<li><strong>Aliases:</strong> cDNA amplification cycles</li>
<li><strong>Subsets:</strong> analysis</li>
</ul>
<p>Number of PCR cycles used during cDNA amplification for this cDNA.</p>
</div>

<div id="cdna-amplification-process-date" class="field-detail">
<h5><code>cDNA amplification process date</code> <em>(optional)</em></h5>
<ul>
<li><strong>BICAN UUID:</strong> <code>6cc333e7-9b98-497f-b7b1-eae904db2400</code></li>
<li><strong>Data Type:</strong> <code>Date</code></li>
<li><strong>Aliases:</strong> cDNA amplification date</li>
</ul>
<p>Date of cDNA amplification.</p>
</div>

<div id="amplified-cdna-rna-amplification-pass-fail" class="field-detail">
<h5><code>amplified cDNA RNA amplification pass-fail</code> <em>(optional)</em></h5>
<ul>
<li><strong>BICAN UUID:</strong> <code>bc62bdb2-7dc8-4404-bb84-ce0bbcae59e5</code></li>
<li><strong>Data Type:</strong> <code>ValueSet</code></li>
<li><strong>Aliases:</strong> cDNA amplification pass-fail result</li>
<li><strong>Subsets:</strong> analysis</li>
</ul>
<p>Pass or Fail result based on qualitative assessment of cDNA yield and size.</p>
</div>

<div id="amplified-cdna-percent-cdna-longer-than-400bp" class="field-detail">
<h5><code>amplified cDNA percent cDNA longer than 400bp</code> <em>(optional)</em></h5>
<ul>
<li><strong>BICAN UUID:</strong> <code>8d150467-f69e-461c-b54c-bcfd22f581e5</code></li>
<li><strong>Data Type:</strong> <code>Float</code></li>
<li><strong>Aliases:</strong> cDNA amplification percent cDNA greater than 400bp</li>
<li><strong>Subsets:</strong> analysis</li>
</ul>
<p>QC metric to measure mRNA degradation of cDNA.  Higher % is higher quality starting material.  Over 400bp is used as a universal cutoff for intact (full length) vs degraded cDNA and is a common output from Bioanalyzer and Fragment Analyzer elecropheragrams.</p>
</div>

<div id="cdna-amplification-set" class="field-detail">
<h5><code>cDNA amplification set</code> <em>(optional)</em></h5>
<ul>
<li><strong>BICAN UUID:</strong> <code>42e98a88-50b3-4ea2-871b-2142f6a0dfdd</code></li>
<li><strong>Data Type:</strong> <code>Text</code></li>
<li><strong>Subsets:</strong> analysis</li>
</ul>
<p>cDNA amplification set, containing multiple amplified_cDNA_names that were processed at the same time.</p>
</div>

#### barcoded cell sample

<div id="barcoded-cell-sample-port-well" class="field-detail">
<h5><code>barcoded cell sample port well</code> <em>(optional)</em></h5>
<ul>
<li><strong>BICAN UUID:</strong> <code>aca38100-d245-4be4-9be3-ba27192779fe</code></li>
<li><strong>Data Type:</strong> <code>Text</code></li>
<li><strong>Aliases:</strong> 10x chip port well</li>
<li><strong>Subsets:</strong> analysis</li>
</ul>
<p>Specific position of the loaded port of the 10x chip.  An Enriched or Dissociated Cell Sample is loaded into a port on a chip (creating a Barcoded Cell Sample).  Can be left null for non-10x methods.</p>
</div>

<div id="barcoded-cell-input-quantity-count" class="field-detail">
<h5><code>barcoded cell input quantity count</code> <em>(optional)</em></h5>
<ul>
<li><strong>BICAN UUID:</strong> <code>aa534269-7c9b-4b63-b990-eea8cda56d0e</code></li>
<li><strong>Data Type:</strong> <code>Integer</code></li>
<li><strong>Subsets:</strong> analysis</li>
</ul>
<p>Number of enriched or dissociated cells/nuclei going into the barcoding process.</p>
</div>

<div id="barcoded-cell-sample-label" class="field-detail">
<h5><code>barcoded cell sample label</code> <em>(required)</em></h5>
<ul>
<li><strong>BICAN UUID:</strong> <code>4c0e6380-e53f-4173-a474-d41e836fefe3</code></li>
<li><strong>Data Type:</strong> <code>Text</code></li>
<li><strong>Aliases:</strong> barcoded cell sample name</li>
<li><strong>Subsets:</strong> analysis, tracking, alignment</li>
</ul>
<p>Name of a collection of barcoded cells.  Input will be either dissociated_cell_sample or enriched_cell_sample.  Cell barcodes are only guaranteed to be unique within this one collection. One dissociated_cell_sample or enriched_cell_sample can lead to multiple barcoded_cell_samples.</p>
</div>

<div id="expected-cell-capture" class="field-detail">
<h5><code>expected cell capture</code> <em>(optional)</em></h5>
<ul>
<li><strong>BICAN UUID:</strong> <code>f10e928d-5a2b-4943-af18-d8fe5d05528d</code></li>
<li><strong>Data Type:</strong> <code>Integer</code></li>
<li><strong>Subsets:</strong> analysis</li>
</ul>
<p>Expected number of cells/nuclei of a barcoded_cell_sample that will be barcoded and available for sequencing.  This is a derived number from &#x27;Barcoded cell input quantity count&#x27; that is dependent on the &quot;capture rate&quot; of the barcoding method.  It is usually a calculated fraction of the &#x27;Barcoded cell input quantity count&#x27; going into the barcoding method.</p>
</div>

<div id="study-sets" class="field-detail">
<h5><code>study sets</code> <em>(optional)</em></h5>
<ul>
<li><strong>BICAN UUID:</strong> <code>8877f8f0-3939-4062-84c9-414bdcdd04ca</code></li>
<li><strong>Data Type:</strong> <code>Text</code></li>
<li><strong>Subsets:</strong> analysis, tracking</li>
</ul>
<p>Intended cohort or dataset that the Barcoded Cell Sample initially belongs to.  This Study helps to group together samples that are meant to be analyzed together.  Multiple Studies can be assigned to a Barcoded Cell Sample.  These studies are more granular than the grant or PI and can be used to group together samples from related ROIs.</p>
</div>

#### dissociated cell sample

<div id="dissociated-cell-sample-cell-prep-type" class="field-detail">
<h5><code>dissociated cell sample cell prep type</code> <em>(required)</em></h5>
<ul>
<li><strong>BICAN UUID:</strong> <code>baae4ac3-f959-4594-b943-3a82ec19bd34</code></li>
<li><strong>Data Type:</strong> <code>ValueSet</code></li>
<li><strong>Aliases:</strong> cell prep type</li>
<li><strong>Subsets:</strong> analysis, tracking</li>
</ul>
<p>The type of cell preparation. For example: Cells, Nuclei. This is a property of dissociated_cell_sample.</p>
</div>

<div id="dissociated-cell-sample-label" class="field-detail">
<h5><code>dissociated cell sample label</code> <em>(optional)</em></h5>
<ul>
<li><strong>BICAN UUID:</strong> <code>65e2c7da-9eb4-45b2-8ccb-d69ef9785ee2</code></li>
<li><strong>Data Type:</strong> <code>Text</code></li>
<li><strong>Aliases:</strong> dissociated cell sample name</li>
<li><strong>Subsets:</strong> analysis</li>
</ul>
<p>Name of a collection of dissociated cells or nuclei derived from dissociation of a tissue sample.</p>
</div>

<div id="dissociated-cell-source-barcode-name" class="field-detail">
<h5><code>dissociated cell source barcode name</code> <em>(optional)</em></h5>
<ul>
<li><strong>BICAN UUID:</strong> <code>184abbaf-baff-4b5f-b51e-dd38de6006af</code></li>
<li><strong>Data Type:</strong> <code>Text</code></li>
<li><strong>Subsets:</strong> ?</li>
</ul>
<p>Name of oligo used in cell plexing.  The oligo will tag allow separate dissociated cell samples to be combined downstream in the barcoded cell sample.  The oligo name is associated with a sequence in a lookup table.  This sequence will be needed to during analysis, after alignment, to associate reads with parent dissociated cell sample.</p>
</div>

<div id="dissociated-cell-source-barcode-name" class="field-detail">
<h5><code>dissociated cell source barcode name</code> <em>(optional)</em></h5>
<ul>
<li><strong>BICAN UUID:</strong> <code>0c8628d0-809b-458c-b4b3-686131dceef8</code></li>
<li><strong>Data Type:</strong> <code>ValueSet</code></li>
<li><strong>Subsets:</strong> analysis</li>
</ul>
<p>Name of oligo used in cell plexing. The oligo will tag allow separate dissociated cell samples to be combined downstream in the barcoded cell sample. The oligo name is associated with a sequence in a lookup table. This sequence will be needed to during analysis, after alignment, to associate reads with parent dissociated cell sample.</p>
</div>

<div id="dissociated-cell-sample-preparation-date" class="field-detail">
<h5><code>dissociated cell sample preparation date</code> <em>(optional)</em></h5>
<ul>
<li><strong>BICAN UUID:</strong> <code>c508b63d-a1b4-42de-9b22-9c4736deac6e</code></li>
<li><strong>Data Type:</strong> <code>Date</code></li>
</ul>
<p>Date of dissociated cell sample creation.</p>
</div>

<div id="patched-cell-structure" class="field-detail">
<h5><code>patched cell structure</code> <em>(optional)</em></h5>
<ul>
<li><strong>BICAN UUID:</strong> <code>7636b4c8-12f6-4b33-bdc6-c2f1a3b1c953</code></li>
<li><strong>Data Type:</strong> <code>ValueSet</code></li>
</ul>
<p>Ontological structure assigned to a single patched cell. This is typically assigned and confirmed after imaging.</p>
</div>

#### enriched cell sample

<div id="enriched-cell-sample-container-name" class="field-detail">
<h5><code>enriched cell sample container name</code> <em>(optional)</em></h5>
<ul>
<li><strong>BICAN UUID:</strong> <code>5ace37aa-85d6-4493-909e-8fc221ec2609</code></li>
<li><strong>Data Type:</strong> <code>Text</code></li>
<li><strong>Subsets:</strong> ?</li>
</ul>
<p>Name of container (strip or tube or plate) of the enriched_cell_prep.  This container could contain 1 or more enriched_cell_samples.</p>
</div>

<div id="enriched-cell-sample-name" class="field-detail">
<h5><code>enriched cell sample name</code> <em>(optional)</em></h5>
<ul>
<li><strong>BICAN UUID:</strong> <code>bb3fc701-23a7-45c1-890d-7471730e0ec1</code></li>
<li><strong>Data Type:</strong> <code>Text</code></li>
<li><strong>Subsets:</strong> analysis</li>
</ul>
<p>Name of collection of enriched cells or nuclei after enrichment process (usually via FACS using the Enrichment Plan) applied to dissociated_cell_sample.</p>
</div>

<div id="enrichment-population" class="field-detail">
<h5><code>enrichment population</code> <em>(optional)</em></h5>
<ul>
<li><strong>BICAN UUID:</strong> <code>875f1c70-f5aa-45e3-94b9-5e482f6c4830</code></li>
<li><strong>Data Type:</strong> <code>Text</code></li>
<li><strong>Subsets:</strong> analysis</li>
</ul>
<p>Actual percentage of cells as a result of using set of fluorescent marker label(s) to enrich dissociated_cell_sample with desired mix of cell populations.  This plan can also be used to describe &#x27;No FACS&#x27; where no enrichment was performed.  This is a property of enriched_cell_prep_container.</p>
</div>

<div id="enriched-cell-source-barcode-name" class="field-detail">
<h5><code>enriched cell source barcode name</code> <em>(optional)</em></h5>
<ul>
<li><strong>BICAN UUID:</strong> <code>bdd5e2bf-c6fa-43e6-a5ac-6878fcf814d6</code></li>
<li><strong>Data Type:</strong> <code>ValueSet</code></li>
<li><strong>Subsets:</strong> alignment</li>
</ul>
<p>Name of molecular barcode used to individual Enriched Cell Source to allow for pooling of Enriched Cell Sources before 10x load (Barcoding Cell step) [aka 1st round barcodes]</p>
</div>

<div id="enriched-cell-sample-preparation-date" class="field-detail">
<h5><code>enriched cell sample preparation date</code> <em>(optional)</em></h5>
<ul>
<li><strong>BICAN UUID:</strong> <code>e2fd2d84-3999-4cc4-8f41-e0e2a708f407</code></li>
<li><strong>Data Type:</strong> <code>Date</code></li>
</ul>
<p>Date of enriched cell sample creation.</p>
</div>

<div id="histone-modification-marker" class="field-detail">
<h5><code>histone modification marker</code> <em>(optional)</em></h5>
<ul>
<li><strong>BICAN UUID:</strong> <code>a2ef2228-e438-4260-95e5-22eb3b35b5a9</code></li>
<li><strong>Data Type:</strong> <code>Text</code></li>
</ul>
<p>Histone modification marker antibodies (eg H3K27ac, H3K27me3, H3K9me3) used in conjunction with an Enriched Cell Source Barcode in order to combine multiple Enriched Cell Populations before Barcoded Cell Sample step for 10xMultiome method. Each of the Histone antibodies captures an essential part of the epigenome.</p>
</div>

#### library

<div id="library-avg-size-bp" class="field-detail">
<h5><code>library avg size bp</code> <em>(optional)</em></h5>
<ul>
<li><strong>BICAN UUID:</strong> <code>f851eba9-56d1-4472-9d0c-d7f8bc33000a</code></li>
<li><strong>Data Type:</strong> <code>Integer</code></li>
<li><strong>Subsets:</strong> analysis</li>
</ul>
<p>Average size of the library in terms of base pairs.  This is used to calculate the molarity before pooling and sequencing.</p>
</div>

<div id="library-method" class="field-detail">
<h5><code>library method</code> <em>(required)</em></h5>
<ul>
<li><strong>BICAN UUID:</strong> <code>7b60d59e-fdd7-4b27-a2d4-cae9b69103a6</code></li>
<li><strong>Data Type:</strong> <code>ValueSet</code></li>
<li><strong>Aliases:</strong> library chemistry method</li>
<li><strong>Subsets:</strong> analysis, tracking, alignment</li>
</ul>
<p>Standardized nomenclature to describe the library method used.  This specifies the alignment method required for the library.  For example, 10xV3.1 (for RNASeq single assay), 10xMult-GEX (for RNASeq multiome assay), and 10xMult-ATAC (for ATACSeq multiome assay)</p>
</div>

<div id="library-concentration-nm" class="field-detail">
<h5><code>library concentration nm</code> <em>(optional)</em></h5>
<ul>
<li><strong>BICAN UUID:</strong> <code>90805b3f-f380-4f23-b159-e7eaa0c8f052</code></li>
<li><strong>Data Type:</strong> <code>Float</code></li>
</ul>
<p>Concentration of library in terms of nM (nMol/L).  Number of molecules is needed for accurate pooling of the libraries and for generating the number of target reads/cell in sequencing.</p>
</div>

<div id="library-creation-date" class="field-detail">
<h5><code>library creation date</code> <em>(optional)</em></h5>
<ul>
<li><strong>BICAN UUID:</strong> <code>9c2f575d-1b64-451d-894f-656861afe07a</code></li>
<li><strong>Data Type:</strong> <code>Date</code></li>
<li><strong>Aliases:</strong> library construction date</li>
</ul>
<p>Date of library construction</p>
</div>

<div id="library-input-ng" class="field-detail">
<h5><code>library input ng</code> <em>(optional)</em></h5>
<ul>
<li><strong>BICAN UUID:</strong> <code>e4d31d97-722d-4771-a0e4-e6062190f2c1</code></li>
<li><strong>Data Type:</strong> <code>Integer</code></li>
<li><strong>Subsets:</strong> analysis</li>
</ul>
<p>Amount of cDNA going into library construction in nanograms.</p>
</div>

<div id="library-label" class="field-detail">
<h5><code>library label</code> <em>(optional)</em></h5>
<ul>
<li><strong>BICAN UUID:</strong> <code>f717e254-3630-4342-be7b-4d56376e7afe</code></li>
<li><strong>Data Type:</strong> <code>Text</code></li>
<li><strong>Aliases:</strong> library name</li>
<li><strong>Subsets:</strong> analysis, tracking</li>
</ul>
<p>Name of a library, which is a collection of fragmented and barcode-indexed DNA molecules for sequencing.  An index or barcode is typically introduced to enable identification of library origin to allow libraries to be pooled together for sequencing.</p>
</div>

<div id="library-prep-pass-fail" class="field-detail">
<h5><code>library prep pass-fail</code> <em>(optional)</em></h5>
<ul>
<li><strong>BICAN UUID:</strong> <code>6817ede2-7ead-402d-9dbc-131aca627c6c</code></li>
<li><strong>Data Type:</strong> <code>ValueSet</code></li>
<li><strong>Aliases:</strong> library prep pass-fail result</li>
<li><strong>Subsets:</strong> analysis</li>
</ul>
<p>Pass or Fail result based on qualitative assessment of library yield and size.</p>
</div>

<div id="library-prep-set" class="field-detail">
<h5><code>library prep set</code> <em>(optional)</em></h5>
<ul>
<li><strong>BICAN UUID:</strong> <code>b124ffa9-9134-4a61-a30d-bb191b2fc7fa</code></li>
<li><strong>Data Type:</strong> <code>Text</code></li>
<li><strong>Subsets:</strong> analysis</li>
</ul>
<p>Library set, containing multiple library_names that were processed at the same time.</p>
</div>

<div id="library-quantification-fmol" class="field-detail">
<h5><code>library quantification fmol</code> <em>(optional)</em></h5>
<ul>
<li><strong>BICAN UUID:</strong> <code>4c09ada7-c116-48bc-8fb1-0dcf5c4b939a</code></li>
<li><strong>Data Type:</strong> <code>Integer</code></li>
<li><strong>Subsets:</strong> analysis</li>
</ul>
<p>Amount of library generated in terms of femtomoles</p>
</div>

<div id="library-quantification-ng" class="field-detail">
<h5><code>library quantification ng</code> <em>(optional)</em></h5>
<ul>
<li><strong>BICAN UUID:</strong> <code>318b2d3a-dae7-4c63-bfbb-93862b92f63e</code></li>
<li><strong>Data Type:</strong> <code>Integer</code></li>
</ul>
<p>Amount of library generated in terms of nanograms</p>
</div>

<div id="r1/r2-index-name" class="field-detail">
<h5><code>R1/R2 index name</code> <em>(required)</em></h5>
<ul>
<li><strong>BICAN UUID:</strong> <code>c94b5d8a-e92d-47af-8c0e-ea3b58be4d06</code></li>
<li><strong>Data Type:</strong> <code>Text</code></li>
<li><strong>Subsets:</strong> analysis, tracking</li>
</ul>
<p>Name of the pair of library indexes used for sequencing.  Indexes allow libraries to be pooled together for sequencing.  Sequencing output (fastq) are demultiplexed by using the indexes for each library.  The name will be associated with the sequences of i7, i5, and i5as, which are needed by SeqCores for demultiplexing.  The required direction of the sequence (sense or antisense) of the index can differ depending on sequencing instruments.</p>
</div>

#### library aliquot

<div id="library-aliquot-label" class="field-detail">
<h5><code>library aliquot label</code> <em>(required)</em></h5>
<ul>
<li><strong>BICAN UUID:</strong> <code>34191bad-d167-4335-8224-ade897d3728e</code></li>
<li><strong>Data Type:</strong> <code>Text</code></li>
<li><strong>Aliases:</strong> library aliquot name</li>
<li><strong>Subsets:</strong> analysis, tracking, alignment</li>
</ul>
<p>One library in the library pool.  Each Library_aliquot_name in a library pool will have a unique R1/R2 index to allow for sequencing together then separating the sequencing output by originating library aliquot through the process of demultiplexing.  The resulting demultiplexed fastq files will include the library_aliquot_name.</p>
</div>

<div id="fastq-file-alignment-status" class="field-detail">
<h5><code>fastq file alignment status</code> <em>(required)</em></h5>
<ul>
<li><strong>BICAN UUID:</strong> <code>834a0e66-fd81-4d9c-b379-146372c3a629</code></li>
<li><strong>Data Type:</strong> <code>ValueSet</code></li>
<li><strong>Aliases:</strong> library aliquot QC result</li>
<li><strong>Subsets:</strong> alignment</li>
</ul>
<p>The QC status of the fastq file alignment process result.</p>
</div>

#### library pool

<div id="library-pool-tube-internal-label" class="field-detail">
<h5><code>library pool tube internal label</code> <em>(required)</em></h5>
<ul>
<li><strong>BICAN UUID:</strong> <code>f1fdea98-7849-4def-a62f-a04cbbf98922</code></li>
<li><strong>Data Type:</strong> <code>Text</code></li>
<li><strong>Aliases:</strong> libray pool tube local name</li>
<li><strong>Subsets:</strong> analysis, tracking</li>
</ul>
<p>Library Pool Tube local name.  Label of the tube containing the library pool, which is made up of multiple library_aliquots.  This is a Library Lab local tube name, before the pool is aliquoted to the Seq Core provided tube &#x27;Library Pool Tube Name&#x27;.</p>
</div>

<div id="embargo-date" class="field-detail">
<h5><code>embargo date</code> <em>(optional)</em></h5>
<ul>
<li><strong>BICAN UUID:</strong> <code>e7bc38d8-7315-40be-b8b7-923bf770ff38</code></li>
<li><strong>Data Type:</strong> <code>Text</code></li>
<li><strong>Subsets:</strong> tracking</li>
</ul>
<p>date until which data much be embargoed</p>
</div>

<div id="seqcore-library-pool-tube-barcode" class="field-detail">
<h5><code>SeqCore library pool tube barcode</code> <em>(required)</em></h5>
<ul>
<li><strong>BICAN UUID:</strong> <code>da02a0ee-9abf-45ef-abb1-981f1aaba6b2</code></li>
<li><strong>Data Type:</strong> <code>Text</code></li>
<li><strong>Subsets:</strong> analysis, tracking</li>
</ul>
<p>Library Pool tube name as provided by the SeqCore (often a barcode).  This tube is provided from the SeqCore and is part of the SeqCore tracking system.</p>
</div>

<div id="library-pool-label" class="field-detail">
<h5><code>library pool label</code> <em>(required)</em></h5>
<ul>
<li><strong>BICAN UUID:</strong> <code>29e0578b-6427-4c93-b29b-bde27fbadeec</code></li>
<li><strong>Data Type:</strong> <code>Text</code></li>
<li><strong>Aliases:</strong> local pool name</li>
<li><strong>Subsets:</strong> analysis, tracking</li>
</ul>
<p>Library lab&#x27;s library pool name.  For some labs this may be the same as &quot;Libray pool tube local name&quot;.   Other labs distinguish between the local tube label of the library pool and the library pool name provided to SeqCore for tracking.  Local Pool Name is used to communicate sequencing status between SeqCore and Library Labs.</p>
</div>

<div id="library-pool-tube-avg-size-bp" class="field-detail">
<h5><code>library pool tube avg size bp</code> <em>(optional)</em></h5>
<ul>
<li><strong>BICAN UUID:</strong> <code>cf1b7c96-cdc1-4eed-8e76-ac44fbd151f7</code></li>
<li><strong>Data Type:</strong> <code>Integer</code></li>
<li><strong>Aliases:</strong> library pool avg size bp</li>
<li><strong>Subsets:</strong> tracking</li>
</ul>
<p>Average insert size of library pool, measured in base pairs.</p>
</div>

<div id="library-pool-fmol" class="field-detail">
<h5><code>library pool fmol</code> <em>(optional)</em></h5>
<ul>
<li><strong>BICAN UUID:</strong> <code>af1a6f3f-aca9-4452-b86e-f3c70c3600b6</code></li>
<li><strong>Data Type:</strong> <code>Float</code></li>
</ul>
<p>Amount of library pool in the tube as measured in femtamoles (fmol)</p>
</div>

<div id="loading-concentration-pm" class="field-detail">
<h5><code>loading concentration pM</code> <em>(optional)</em></h5>
<ul>
<li><strong>BICAN UUID:</strong> <code>a1a1b046-549d-4e94-9b3c-5fac2a31fdd6</code></li>
<li><strong>Data Type:</strong> <code>Float</code></li>
</ul>
<p>Sequencer Loading Concentration as measured in pM (pmol/L).  This is a value used by the SeqCore.</p>
</div>

<div id="length-of-read-2-(for-paired-end-runs)" class="field-detail">
<h5><code>length of Read 2 (for Paired End Runs)</code> <em>(required)</em></h5>
<ul>
<li><strong>BICAN UUID:</strong> <code>0b9a9cbc-b8dd-42a2-a567-aafd9370db30</code></li>
<li><strong>Data Type:</strong> <code>Integer</code></li>
<li><strong>Subsets:</strong> analysis, tracking, alignment</li>
</ul>
<p>Separate field to replace the combined field &quot;Sequencing cycle&quot;. Sequencing Cycle is needed for sequencing the library pool.  The sequencing cycle needed is specific to the Library Chemistry Method and is required instruction to the SeqCores.</p>
</div>

<div id="length-of-index-1-(i7-primer)" class="field-detail">
<h5><code>length of Index 1 (i7 Primer)</code> <em>(required)</em></h5>
<ul>
<li><strong>BICAN UUID:</strong> <code>0b94df0d-d96e-4d49-a498-b3eb83afc5f8</code></li>
<li><strong>Data Type:</strong> <code>Integer</code></li>
<li><strong>Subsets:</strong> analysis, tracking, alignment</li>
</ul>
<p>Separate field to replace the combined field &quot;Sequencing cycle&quot;. Sequencing Cycle is needed for sequencing the library pool.  The sequencing cycle needed is specific to the Library Chemistry Method and is required instruction to the SeqCores.</p>
</div>

<div id="length-of-index-2-(i5-primer)" class="field-detail">
<h5><code>length of Index 2 (i5 Primer)</code> <em>(required)</em></h5>
<ul>
<li><strong>BICAN UUID:</strong> <code>a61c1d55-b880-499c-ba4a-30311fdca62f</code></li>
<li><strong>Data Type:</strong> <code>Integer</code></li>
<li><strong>Subsets:</strong> analysis, tracking, alignment</li>
</ul>
<p>Separate field to replace the combined field &quot;Sequencing cycle&quot;. Sequencing Cycle is needed for sequencing the library pool.  The sequencing cycle needed is specific to the Library Chemistry Method and is required instruction to the SeqCores.</p>
</div>

<div id="length-of-read-1" class="field-detail">
<h5><code>length of Read 1</code> <em>(required)</em></h5>
<ul>
<li><strong>BICAN UUID:</strong> <code>f22ac08a-bb81-4524-91f0-0e1e1a032335</code></li>
<li><strong>Data Type:</strong> <code>Integer</code></li>
<li><strong>Subsets:</strong> analysis, tracking, alignment</li>
</ul>
<p>Separate field to replace the combined field &quot;Sequencing cycle&quot;. Sequencing Cycleis  needed for sequencing the library pool.  The sequencing cycle needed is specific to the Library Chemistry Method and is required instruction to the SeqCores.</p>
</div>

<div id="library-pool-tube-contents-nm" class="field-detail">
<h5><code>library pool tube contents nM</code> <em>(optional)</em></h5>
<ul>
<li><strong>BICAN UUID:</strong> <code>32f2d02b-7300-4554-aa93-6de6e456eda7</code></li>
<li><strong>Data Type:</strong> <code>Float</code></li>
<li><strong>Aliases:</strong> library pool concentration (nM)</li>
<li><strong>Subsets:</strong> tracking</li>
</ul>
<p>Library pool concentration as measured in nanomolarity (nMol/L)</p>
</div>

<div id="library-pool-tube-volume-ul" class="field-detail">
<h5><code>library pool tube volume ul</code> <em>(optional)</em></h5>
<ul>
<li><strong>BICAN UUID:</strong> <code>b1b923ac-c218-4db4-a3b1-45a219612567</code></li>
<li><strong>Data Type:</strong> <code>Integer</code></li>
<li><strong>Subsets:</strong> tracking</li>
</ul>
<p>Library pool volume as measured in ul</p>
</div>

<div id="phix-spike-in-percent" class="field-detail">
<h5><code>PhiX spike in percent</code> <em>(optional)</em></h5>
<ul>
<li><strong>BICAN UUID:</strong> <code>b5ab26ad-d523-406e-a85b-e77f2f4b06b5</code></li>
<li><strong>Data Type:</strong> <code>Float</code></li>
</ul>
<p>PhiX spike-in percent desired to be added to the library pool for sequencing.  PhiX is used to increase complexity of the sample being sequenced, to reduce sequencing artifacts maintain sequencing quality on the instruments.  This is an optional instruction to the SeqCore.</p>
</div>

<div id="custom-primers" class="field-detail">
<h5><code>custom primers</code> <em>(optional)</em></h5>
<ul>
<li><strong>BICAN UUID:</strong> <code>76c905d5-ef4a-421a-bd59-b541c5c1d45d</code></li>
<li><strong>Data Type:</strong> <code>Boolean</code></li>
<li><strong>Subsets:</strong> tracking, alignment</li>
</ul>
<p>Custom sequencing primers if needed, indicate with reads require them (R1/R2/i7/i5)</p>
</div>

<div id="library-pool-construction-date" class="field-detail">
<h5><code>library pool construction date</code> <em>(optional)</em></h5>
<ul>
<li><strong>BICAN UUID:</strong> <code>ef950ca1-2a62-4fce-a826-6c27d94d3be3</code></li>
<li><strong>Data Type:</strong> <code>Date</code></li>
</ul>
<p>Date of library pool construction.</p>
</div>

<div id="flowcell" class="field-detail">
<h5><code>flowcell</code> <em>(optional)</em></h5>
<ul>
<li><strong>BICAN UUID:</strong> <code>4c8d7ac8-d3e3-4177-a93d-18ec2302c392</code></li>
<li><strong>Data Type:</strong> <code>Text</code></li>
</ul>
<p></p>
</div>

#### tissue sample

<div id="tissue-sample-label" class="field-detail">
<h5><code>tissue sample label</code> <em>(required)</em></h5>
<ul>
<li><strong>BICAN UUID:</strong> <code>2e4ca2fc-2d77-4d19-af45-d0fb7bbc2269</code></li>
<li><strong>Data Type:</strong> <code>text</code></li>
<li><strong>Aliases:</strong> tissue name|tissue sample label</li>
<li><strong>Subsets:</strong> analysis, tracking</li>
</ul>
<p>Identifier name for final intact piece of tissue before cell or nuclei prep.  This piece of tissue will be used in dissociation and has an ROI associated with it.</p>
</div>

<!-- schema-properties-end -->

## Changelog

### Version 1.2.1

- 1.2.1 Added 'pass' as a value to library QC result.

### Version 1.2

#### Added

- 1.2 patched cell structure

### Version 1.1.1

#### Changed

- 1.1.1 Changed fastq file alignment status value set (Pass to Pass-Flag)

### Version 1.1

#### Added

- 1.1 dissociated_cell_sample_preparation_date
- 1.1 dissociated_cell_sample_cell_label_barcode
- 1.1 enriched_cell_sample_cell_label_barcode
- 1.1 enriched_cell_sample_preparation_date
- 1.1 histone_modification_marker
- 1.1 library_pool_preparation_date
- 1.1 flowcell

