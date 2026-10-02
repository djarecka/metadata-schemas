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

#### Amplified cDNA

| Property | Type | Required | Aliases | Description |
|----------|------|----------|---------|-------------|
| [`amplified cdna NHash ID`](#amplified-cdna-nhash-id) | text | yes | — | NIMP generated globally unique identifier for Amplified cDNA |
| [`project identifier`](#project-identifier) | integer | yes | — | NIMP database id for the project this amplified cDNA belongs to |
| [`amplified cDNA amplified quantity ng`](#amplified-cdna-amplified-quantity-ng) | float | no | amplified quantity ng | Amount of cDNA produced after cDNA amplification measured in nanograms |
| [`amplified cDNA PCR cycles`](#amplified-cdna-pcr-cycles) | integer | no | cDNA amplification cycles | Number of PCR cycles used during cDNA amplification for this cDNA. |
| [`amplified cDNA RNA amplification pass-fail`](#amplified-cdna-rna-amplification-pass-fail) | categorical | no | cDNA amplification pass-fail result | Pass or Fail result based on qualitative assessment of cDNA yield and size. |
| [`amplified cDNA percent cDNA longer than 400bp`](#amplified-cdna-percent-cdna-longer-than-400bp) | float | no | cDNA amplification percent cDNA greater than 400bp | QC metric to measure mRNA degradation of cDNA. Higher % is higher quality starting material. Over 400bp is used as a uni… |
| [`amplified cdna project`](#amplified-cdna-project) | categorical | yes | — | Amplified cDNA Project |
| [`amplified cdna lab`](#amplified-cdna-lab) | categorical | yes | — | Amplified cDNA Lab |

#### Barcoded Cell Sample

| Property | Type | Required | Aliases | Description |
|----------|------|----------|---------|-------------|
| [`barcoded cell sample NHash ID`](#barcoded-cell-sample-nhash-id) | text | yes | — | NIMP generated globally unique identifier for a Barcoded Cell Sample |
| [`barcoded cell sample number of expected cells`](#barcoded-cell-sample-number-of-expected-cells) | integer | no | — | Expected number of cells/nuclei of a barcoded_cell_sample that will be barcoded and available for sequencing. This is a … |
| [`project identifier`](#project-identifier) | integer | yes | — | NIMP database id for the project this Barcoded Cell Sample belongs to |
| [`barcoded cell sample port well`](#barcoded-cell-sample-port-well) | text | no | 10x chip port well | Specific position of the loaded port of the 10x chip. An Enriched or Dissociated Cell Sample is loaded into a port on a … |
| [`barcoded cell input quantity count`](#barcoded-cell-input-quantity-count) | integer | no | — | Number of enriched or dissociated cells/nuclei going into the barcoding process. |
| [`barcoded cell sample technique`](#barcoded-cell-sample-technique) | categorical | yes | — | Required standardized nomenclature to describe the general method used to barcode individual cells. This method (eg Mult… |
| [`barcoded cell sample tag local name`](#barcoded-cell-sample-tag-local-name) | text | no | — | Barcoded Cell Sample tags can be used to group a set of barcoded cell samples so that the tag can be used to obtain all … |
| [`barcoded cell sample project`](#barcoded-cell-sample-project) | categorical | yes | — | Barcoded Cell Sample Project |
| [`barcoded cell sample lab`](#barcoded-cell-sample-lab) | categorical | yes | — | Barcoded Cell Sample Lab |
| [`bcs alignment job ID`](#bcs-alignment-job-id) | text | no | — | Barcoded Cell Sample Alignment QC Job ID |
| [`barcoded cell sample alignment QC status`](#barcoded-cell-sample-alignment-qc-status) | categorical | no | — | Barcoded Cell Sample alignment QC status |

#### Dissociated Cell Sample

| Property | Type | Required | Aliases | Description |
|----------|------|----------|---------|-------------|
| [`dissociated cell sample NHash ID`](#dissociated-cell-sample-nhash-id) | text | yes | — | NIMP generated globally unique identifier for a Dissociated Cell Sample |
| [`dissociated cell sample cell label barcode`](#dissociated-cell-sample-cell-label-barcode) | categorical | no | dissociated cell source barcode name | Name of oligo used in cell plexing. The oligo will tag allow separate dissociated cell samples to be combined downstream… |
| [`dissociated cell sample cell prep type`](#dissociated-cell-sample-cell-prep-type) | categorical | no | cell prep type | The type of cell preparation. For example: Cells; Nuclei. This is a property of dissociated_cell_sample. |
| [`project identifier`](#project-identifier) | integer | yes | — | NIMP database id of the project the dissociated cell sample is associated with |
| [`tissue NHash IDs`](#tissue-nhash-ids) | text | yes | — | NIMP generated globally unique identifier for upstream tissues |
| [`patched cell structure`](#patched-cell-structure) | categorical | no | — | Ontological structure assigned to a single patched cell.  This is typically assigned and confirmed after imaging. |
| [`dissociated cell sample project`](#dissociated-cell-sample-project) | categorical | yes | — | Dissociated Cell Sample Project |
| [`dissociated cell sample lab`](#dissociated-cell-sample-lab) | categorical | yes | — | Dissociated Cell Sample Lab |

#### Enriched Cell Sample

| Property | Type | Required | Aliases | Description |
|----------|------|----------|---------|-------------|
| [`enriched cell sample NHash ID`](#enriched-cell-sample-nhash-id) | text | yes | — | NIMP generated globally unique identifier for an Enriched Cell Sample |
| [`enriched cell sample cell label barcode`](#enriched-cell-sample-cell-label-barcode) | categorical | no | enriched cell source barcode name | Name of molecular barcode used to individual Enriched Cell Source to allow for pooling of Enriched Cell Sources before 1… |
| [`project identifier`](#project-identifier) | integer | yes | — | NIMP database id for the project his Enriched Cell Sample is associated with |
| [`enrichment population`](#enrichment-population) | text | no | — | Actual percentage of cells as a result of using set of fluorescent marker label(s) to enrich dissociated_cell_sample wit… |
| [`histone modification marker`](#histone-modification-marker) | text | no | — | Histone modification marker antibodies (eg H3K27ac; H3K27me3; H3K9me3) used in conjunction with an Enriched Cell Source … |
| [`enriched cell sample project`](#enriched-cell-sample-project) | categorical | yes | — | Enriched Cell Sample Project |
| [`enriched cell sample lab`](#enriched-cell-sample-lab) | categorical | yes | — | Enriched Cell Sample Lab |

#### Library

| Property | Type | Required | Aliases | Description |
|----------|------|----------|---------|-------------|
| [`library NHash ID`](#library-nhash-id) | text | yes | — | NIMP generated globally unique identifier for a Library |
| [`library technique`](#library-technique) | categorical | yes | library method; library chemistry method | Standardized nomenclature to describe the library method used. This specifies the alignment method required for the libr… |
| [`library r1/r2 index`](#library-r1/r2-index) | categorical | no | R1/R2 index name | Name of the pair of library indexes used for sequencing. Indexes allow libraries to be pooled together for sequencing. S… |
| [`library source type`](#library-source-type) | categorical | no | — | The upstream resource type for library creation. Could be either Barcoded Cell Samples or Amplified cDNA |
| [`project identifier`](#project-identifier) | integer | yes | — | NIMP database id for the project this Library is associated with |
| [`library avg size bp`](#library-avg-size-bp) | integer | no | — | Average size of the library in terms of base pairs. This is used to calculate the molarity before pooling and sequencing… |
| [`library concentration nm`](#library-concentration-nm) | float | no | — | Concentration of library in terms of nM (nMol/L). Number of molecules is needed for accurate pooling of the libraries an… |
| [`library input ng`](#library-input-ng) | float | no | — | Amount of cDNA going into library construction in nanograms. |
| [`library prep pass-fail`](#library-prep-pass-fail) | categorical | no | library prep pass-fail result | Pass or Fail result based on qualitative assessment of library yield and size. |
| [`library quantification fmol`](#library-quantification-fmol) | float | no | — | Amount of library generated in terms of femtomoles |
| [`library quantification ng`](#library-quantification-ng) | float | no | — | Amount of library generated in terms of nanograms |
| [`library project`](#library-project) | categorical | yes | — | Library Project |
| [`library lab`](#library-lab) | categorical | yes | — | Library Lab |

#### Library Aliquot

| Property | Type | Required | Aliases | Description |
|----------|------|----------|---------|-------------|
| [`library aliquot local name`](#library-aliquot-local-name) | text | yes | library aliquot label | One library in the library pool. Each Library_aliquot_name in a library pool will have a unique R1/R2 index to allow for… |
| [`library aliquot NHash ID`](#library-aliquot-nhash-id) | text | yes | — | NIMP generated globally unique identifier for a Library Aliquot. This NHash id is a concatenation of the NHash ids of th… |
| [`sequencing result date`](#sequencing-result-date) | date | no | — | The date of sequencing results for the Library Aliquot as reported by the Sequencing Center |
| [`library aliquot sequencing result status`](#library-aliquot-sequencing-result-status) | categorical | no | — | The status of the sequencing results for the Library Aliquot as reported by the Sequencing Center |
| [`fastq file alignment status`](#fastq-file-alignment-status) | categorical | no | — | The FASTQ file alignment status as reported by the Library Lab |
| [`library aliquot fastq file size in TB`](#library-aliquot-fastq-file-size-in-tb) | integer | no | — | Library Aliquot FASTQ File Size in TB |
| [`library aliquot project`](#library-aliquot-project) | categorical | yes | — | Library Aliquot Project |
| [`library aliquot lab`](#library-aliquot-lab) | categorical | yes | — | Library Aliquot Lab |
| [`alignment QC status`](#alignment-qc-status) | categorical | no | — | Library Aliquot Alignment QC Status |
| [`NeMO aliquot fastq public URL`](#nemo-aliquot-fastq-public-url) | text | no | — | NeMO Aliquot Fastq Public URL |
| [`NeMO aliquot fastq gcp URL`](#nemo-aliquot-fastq-gcp-url) | text | no | — | NeMO Aliquot Fastq GCP URL |
| [`aliquot alignment job ID`](#aliquot-alignment-job-id) | text | no | — | Library Aliquot Alignment QC Job ID |
| [`library aliquot QC last updated date`](#library-aliquot-qc-last-updated-date) | date | no | — | Library Aliquot QC last updated date |
| [`aliquot alignment QC uploaded date`](#aliquot-alignment-qc-uploaded-date) | date | no | — | Library Aliquot alignment QC uploaded date |
| [`aliquot QC total reads`](#aliquot-qc-total-reads) | integer | no | — | Library Aliquot QC total reads |

#### Library Package

| Property | Type | Required | Aliases | Description |
|----------|------|----------|---------|-------------|
| [`sequencing center ID`](#sequencing-center-id) | categorical | yes | — | NIMP id for the Sequencing Center this Library Package will be sent to. |

#### Library Pool

| Property | Type | Required | Aliases | Description |
|----------|------|----------|---------|-------------|
| [`library pool NHash ID`](#library-pool-nhash-id) | text | yes | — | NIMP generated globally unique identifier for a Library Pool |
| [`library pool tube barcode`](#library-pool-tube-barcode) | text | no | SeqCore library pool tube barcode | Library Pool tube name as provided by the SeqCore (often a barcode). This tube is provided from the SeqCore and is part … |
| [`flowcell`](#flowcell) | text | no | — | The Flowcell is a unique identifer of the sequencing cartridge (provided by the sequencing instrument manufacturer) used… |
| [`library pool alignment status`](#library-pool-alignment-status) | categorical | no | — | Whether the Library Pool is approved for alignment or not |
| [`library pool sequencing instrument`](#library-pool-sequencing-instrument) | categorical | no | — | Library Pool Sequencing Instrument |
| [`library pool flowcell type`](#library-pool-flowcell-type) | categorical | no | — | Library Pool Flowcell Type |
| [`library pool fastq submission ID`](#library-pool-fastq-submission-id) | text | no | — | Library Pool FASTQ Submission ID |
| [`library pool projects`](#library-pool-projects) | categorical | yes | — | Library Pool Projects |
| [`library pool labs`](#library-pool-labs) | categorical | yes | — | Library Pool Labs |
| [`NeMO pool bucket`](#nemo-pool-bucket) | text | no | — | Nemo Pool Bucket |

#### The LINKML class or data entity (e.g. purple or orange box in the workflow diagram) with which this metadata field is associated

| Property | Type | Required | Aliases | Description |
|----------|------|----------|---------|-------------|
| [`Name of metadata field`](#name-of-metadata-field) | Type of values in this field (integer; float; text; date) | no | Aliases for this metadata element in other schemas/resources | A detailed definition for this field |

### Property Details

#### Amplified cDNA

<div id="amplified-cdna-nhash-id" class="field-detail">
<h5><code>amplified cdna NHash ID</code> <em>(required)</em></h5>
<ul>
<li><strong>BICAN UUID:</strong> <code>01046de6-448d-4f50-a794-0a5ffb2bcf97</code></li>
<li><strong>Data Type:</strong> <code>text</code></li>
</ul>
<p>NIMP generated globally unique identifier for Amplified cDNA</p>
</div>

<div id="project-identifier" class="field-detail">
<h5><code>project identifier</code> <em>(required)</em></h5>
<ul>
<li><strong>BICAN UUID:</strong> <code>9a55368b-3b12-47f3-a3cb-ee282c6d73ce</code></li>
<li><strong>Data Type:</strong> <code>integer</code></li>
</ul>
<p>NIMP database id for the project this amplified cDNA belongs to</p>
</div>

<div id="amplified-cdna-amplified-quantity-ng" class="field-detail">
<h5><code>amplified cDNA amplified quantity ng</code> <em>(optional)</em></h5>
<ul>
<li><strong>BICAN UUID:</strong> <code>0db79d05-8612-4896-b9d3-eb1558841449</code></li>
<li><strong>Data Type:</strong> <code>float</code></li>
<li><strong>Aliases:</strong> amplified quantity ng</li>
<li><strong>Subsets:</strong> analysis</li>
<li><strong>Range:</strong> 0 – —</li>
</ul>
<p>Amount of cDNA produced after cDNA amplification measured in nanograms</p>
</div>

<div id="amplified-cdna-pcr-cycles" class="field-detail">
<h5><code>amplified cDNA PCR cycles</code> <em>(optional)</em></h5>
<ul>
<li><strong>BICAN UUID:</strong> <code>3827634c-3f8f-4760-b358-86ce4b030238</code></li>
<li><strong>Data Type:</strong> <code>integer</code></li>
<li><strong>Aliases:</strong> cDNA amplification cycles</li>
<li><strong>Subsets:</strong> analysis</li>
<li><strong>Range:</strong> 0 – —</li>
</ul>
<p>Number of PCR cycles used during cDNA amplification for this cDNA.</p>
</div>

<div id="amplified-cdna-rna-amplification-pass-fail" class="field-detail">
<h5><code>amplified cDNA RNA amplification pass-fail</code> <em>(optional)</em></h5>
<ul>
<li><strong>BICAN UUID:</strong> <code>bc62bdb2-7dc8-4404-bb84-ce0bbcae59e5</code></li>
<li><strong>Data Type:</strong> <code>categorical</code></li>
<li><strong>Aliases:</strong> cDNA amplification pass-fail result</li>
<li><strong>Subsets:</strong> analysis</li>
</ul>
<p>Pass or Fail result based on qualitative assessment of cDNA yield and size.</p>
<p><strong>Permissible values:</strong> <code>Yes</code></p>
</div>

<div id="amplified-cdna-percent-cdna-longer-than-400bp" class="field-detail">
<h5><code>amplified cDNA percent cDNA longer than 400bp</code> <em>(optional)</em></h5>
<ul>
<li><strong>BICAN UUID:</strong> <code>8d150467-f69e-461c-b54c-bcfd22f581e5</code></li>
<li><strong>Data Type:</strong> <code>float</code></li>
<li><strong>Aliases:</strong> cDNA amplification percent cDNA greater than 400bp</li>
<li><strong>Subsets:</strong> analysis</li>
<li><strong>Range:</strong> 0 – —</li>
</ul>
<p>QC metric to measure mRNA degradation of cDNA. Higher % is higher quality starting material. Over 400bp is used as a universal cutoff for intact (full length) vs degraded cDNA and is a common output from Bioanalyzer and Fragment Analyzer elecropheragrams.</p>
</div>

<div id="amplified-cdna-project" class="field-detail">
<h5><code>amplified cdna project</code> <em>(required)</em></h5>
<ul>
<li><strong>BICAN UUID:</strong> <code>20f516dc-ed4f-494e-9959-d01f286171fc</code></li>
<li><strong>Data Type:</strong> <code>categorical</code></li>
</ul>
<p>Amplified cDNA Project</p>
<p><strong>Permissible values:</strong> <code>Yes</code></p>
</div>

<div id="amplified-cdna-lab" class="field-detail">
<h5><code>amplified cdna lab</code> <em>(required)</em></h5>
<ul>
<li><strong>BICAN UUID:</strong> <code>88b13d5b-3b06-4294-9b83-b4b615c6085e</code></li>
<li><strong>Data Type:</strong> <code>categorical</code></li>
</ul>
<p>Amplified cDNA Lab</p>
<p><strong>Permissible values:</strong> <code>Yes</code></p>
</div>

#### Barcoded Cell Sample

<div id="barcoded-cell-sample-nhash-id" class="field-detail">
<h5><code>barcoded cell sample NHash ID</code> <em>(required)</em></h5>
<ul>
<li><strong>BICAN UUID:</strong> <code>b421ecfe-488e-4e87-bf4c-6d30aa5b06bb</code></li>
<li><strong>Data Type:</strong> <code>text</code></li>
</ul>
<p>NIMP generated globally unique identifier for a Barcoded Cell Sample</p>
</div>

<div id="barcoded-cell-sample-number-of-expected-cells" class="field-detail">
<h5><code>barcoded cell sample number of expected cells</code> <em>(optional)</em></h5>
<ul>
<li><strong>BICAN UUID:</strong> <code>f10e928d-5a2b-4943-af18-d8fe5d05528d</code></li>
<li><strong>Data Type:</strong> <code>integer</code></li>
<li><strong>Subsets:</strong> analysis</li>
<li><strong>Range:</strong> 0 – —</li>
</ul>
<p>Expected number of cells/nuclei of a barcoded_cell_sample that will be barcoded and available for sequencing. This is a derived number from &#x27;Barcoded cell input quantity count&#x27; that is dependent on the &quot;capture rate&quot; of the barcoding method. It is usually a calculated fraction of the &#x27;Barcoded cell input quantity count&#x27; going into the barcoding method.</p>
</div>

<div id="project-identifier" class="field-detail">
<h5><code>project identifier</code> <em>(required)</em></h5>
<ul>
<li><strong>BICAN UUID:</strong> <code>9a55368b-3b12-47f3-a3cb-ee282c6d73ce</code></li>
<li><strong>Data Type:</strong> <code>integer</code></li>
</ul>
<p>NIMP database id for the project this Barcoded Cell Sample belongs to</p>
</div>

<div id="barcoded-cell-sample-port-well" class="field-detail">
<h5><code>barcoded cell sample port well</code> <em>(optional)</em></h5>
<ul>
<li><strong>BICAN UUID:</strong> <code>aca38100-d245-4be4-9be3-ba27192779fe</code></li>
<li><strong>Data Type:</strong> <code>text</code></li>
<li><strong>Aliases:</strong> 10x chip port well</li>
<li><strong>Subsets:</strong> analysis</li>
</ul>
<p>Specific position of the loaded port of the 10x chip. An Enriched or Dissociated Cell Sample is loaded into a port on a chip (creating a Barcoded Cell Sample). Can be left null for non-10x methods.</p>
</div>

<div id="barcoded-cell-input-quantity-count" class="field-detail">
<h5><code>barcoded cell input quantity count</code> <em>(optional)</em></h5>
<ul>
<li><strong>BICAN UUID:</strong> <code>aa534269-7c9b-4b63-b990-eea8cda56d0e</code></li>
<li><strong>Data Type:</strong> <code>integer</code></li>
<li><strong>Subsets:</strong> analysis</li>
<li><strong>Range:</strong> 0 – —</li>
</ul>
<p>Number of enriched or dissociated cells/nuclei going into the barcoding process.</p>
</div>

<div id="barcoded-cell-sample-technique" class="field-detail">
<h5><code>barcoded cell sample technique</code> <em>(required)</em></h5>
<ul>
<li><strong>BICAN UUID:</strong> <code>b2366423-b883-4b33-b036-a1e4707c32bd</code></li>
<li><strong>Data Type:</strong> <code>categorical</code></li>
</ul>
<p>Required standardized nomenclature to describe the general method used to barcode individual cells. This method (eg Multiome; ATAConly; GEXonly) will be more general than the Library Method (which is specific for alignment) and could be used for general classification of Barcoded Cell Samples.</p>
<p><strong>Permissible values:</strong> <code>Yes</code></p>
</div>

<div id="barcoded-cell-sample-tag-local-name" class="field-detail">
<h5><code>barcoded cell sample tag local name</code> <em>(optional)</em></h5>
<ul>
<li><strong>BICAN UUID:</strong> <code>8877f8f0-3939-4062-84c9-414bdcdd04ca</code></li>
<li><strong>Data Type:</strong> <code>text</code></li>
<li><strong>Subsets:</strong> analysis; tracking</li>
</ul>
<p>Barcoded Cell Sample tags can be used to group a set of barcoded cell samples so that the tag can be used to obtain all the members of the cohort</p>
</div>

<div id="barcoded-cell-sample-project" class="field-detail">
<h5><code>barcoded cell sample project</code> <em>(required)</em></h5>
<ul>
<li><strong>BICAN UUID:</strong> <code>b5f4485b-3700-460d-8455-016127783ccb</code></li>
<li><strong>Data Type:</strong> <code>categorical</code></li>
</ul>
<p>Barcoded Cell Sample Project</p>
<p><strong>Permissible values:</strong> <code>Yes</code></p>
</div>

<div id="barcoded-cell-sample-lab" class="field-detail">
<h5><code>barcoded cell sample lab</code> <em>(required)</em></h5>
<ul>
<li><strong>BICAN UUID:</strong> <code>f73165f0-8540-4ed0-91fd-ff2ce946ebcb</code></li>
<li><strong>Data Type:</strong> <code>categorical</code></li>
</ul>
<p>Barcoded Cell Sample Lab</p>
<p><strong>Permissible values:</strong> <code>Yes</code></p>
</div>

<div id="bcs-alignment-job-id" class="field-detail">
<h5><code>bcs alignment job ID</code> <em>(optional)</em></h5>
<ul>
<li><strong>BICAN UUID:</strong> <code>12ef6c0b-7db5-451f-8e84-a9fcd8086a2e</code></li>
<li><strong>Data Type:</strong> <code>text</code></li>
</ul>
<p>Barcoded Cell Sample Alignment QC Job ID</p>
</div>

<div id="barcoded-cell-sample-alignment-qc-status" class="field-detail">
<h5><code>barcoded cell sample alignment QC status</code> <em>(optional)</em></h5>
<ul>
<li><strong>BICAN UUID:</strong> <code>a0f07acd-df7c-4dce-9bdf-313ce84b4ead</code></li>
<li><strong>Data Type:</strong> <code>categorical</code></li>
</ul>
<p>Barcoded Cell Sample alignment QC status</p>
<p><strong>Permissible values:</strong> <code>Yes</code></p>
</div>

#### Dissociated Cell Sample

<div id="dissociated-cell-sample-nhash-id" class="field-detail">
<h5><code>dissociated cell sample NHash ID</code> <em>(required)</em></h5>
<ul>
<li><strong>BICAN UUID:</strong> <code>9b18ee42-7e93-44f1-a1d3-f811eb3b777b</code></li>
<li><strong>Data Type:</strong> <code>text</code></li>
</ul>
<p>NIMP generated globally unique identifier for a Dissociated Cell Sample</p>
</div>

<div id="dissociated-cell-sample-cell-label-barcode" class="field-detail">
<h5><code>dissociated cell sample cell label barcode</code> <em>(optional)</em></h5>
<ul>
<li><strong>BICAN UUID:</strong> <code>0c8628d0-809b-458c-b4b3-686131dceef8</code></li>
<li><strong>Data Type:</strong> <code>categorical</code></li>
<li><strong>Aliases:</strong> dissociated cell source barcode name</li>
<li><strong>Subsets:</strong> analysis</li>
</ul>
<p>Name of oligo used in cell plexing. The oligo will tag allow separate dissociated cell samples to be combined downstream in the barcoded cell sample. The oligo name is associated with a sequence in a lookup table. This sequence will be needed to during analysis (after alignment) to associate reads with parent dissociated cell sample.</p>
<p><strong>Permissible values:</strong> <code>Yes</code></p>
</div>

<div id="dissociated-cell-sample-cell-prep-type" class="field-detail">
<h5><code>dissociated cell sample cell prep type</code> <em>(optional)</em></h5>
<ul>
<li><strong>BICAN UUID:</strong> <code>baae4ac3-f959-4594-b943-3a82ec19bd34</code></li>
<li><strong>Data Type:</strong> <code>categorical</code></li>
<li><strong>Aliases:</strong> cell prep type</li>
<li><strong>Subsets:</strong> analysis; tracking</li>
</ul>
<p>The type of cell preparation. For example: Cells; Nuclei. This is a property of dissociated_cell_sample.</p>
<p><strong>Permissible values:</strong> <code>Yes</code></p>
</div>

<div id="project-identifier" class="field-detail">
<h5><code>project identifier</code> <em>(required)</em></h5>
<ul>
<li><strong>BICAN UUID:</strong> <code>9a55368b-3b12-47f3-a3cb-ee282c6d73ce</code></li>
<li><strong>Data Type:</strong> <code>integer</code></li>
</ul>
<p>NIMP database id of the project the dissociated cell sample is associated with</p>
</div>

<div id="tissue-nhash-ids" class="field-detail">
<h5><code>tissue NHash IDs</code> <em>(required)</em></h5>
<ul>
<li><strong>BICAN UUID:</strong> <code>8b10c5a7-a1c8-488f-9a7c-a80fd801db3c</code></li>
<li><strong>Data Type:</strong> <code>text</code></li>
</ul>
<p>NIMP generated globally unique identifier for upstream tissues</p>
</div>

<div id="patched-cell-structure" class="field-detail">
<h5><code>patched cell structure</code> <em>(optional)</em></h5>
<ul>
<li><strong>BICAN UUID:</strong> <code>7636b4c8-12f6-4b33-bdc6-c2f1a3b1c953</code></li>
<li><strong>Data Type:</strong> <code>categorical</code></li>
</ul>
<p>Ontological structure assigned to a single patched cell.  This is typically assigned and confirmed after imaging.</p>
<p><strong>Permissible values:</strong> <code>Yes</code></p>
</div>

<div id="dissociated-cell-sample-project" class="field-detail">
<h5><code>dissociated cell sample project</code> <em>(required)</em></h5>
<ul>
<li><strong>BICAN UUID:</strong> <code>80976c95-c329-496e-8c5b-f9d48b6cf189</code></li>
<li><strong>Data Type:</strong> <code>categorical</code></li>
</ul>
<p>Dissociated Cell Sample Project</p>
<p><strong>Permissible values:</strong> <code>Yes</code></p>
</div>

<div id="dissociated-cell-sample-lab" class="field-detail">
<h5><code>dissociated cell sample lab</code> <em>(required)</em></h5>
<ul>
<li><strong>BICAN UUID:</strong> <code>b94f6f31-8ac0-40b5-861f-86c3112bf1b8</code></li>
<li><strong>Data Type:</strong> <code>categorical</code></li>
</ul>
<p>Dissociated Cell Sample Lab</p>
<p><strong>Permissible values:</strong> <code>Yes</code></p>
</div>

#### Enriched Cell Sample

<div id="enriched-cell-sample-nhash-id" class="field-detail">
<h5><code>enriched cell sample NHash ID</code> <em>(required)</em></h5>
<ul>
<li><strong>BICAN UUID:</strong> <code>ba153086-53ce-48e5-a2ed-e355a0ff0cc3</code></li>
<li><strong>Data Type:</strong> <code>text</code></li>
</ul>
<p>NIMP generated globally unique identifier for an Enriched Cell Sample</p>
</div>

<div id="enriched-cell-sample-cell-label-barcode" class="field-detail">
<h5><code>enriched cell sample cell label barcode</code> <em>(optional)</em></h5>
<ul>
<li><strong>BICAN UUID:</strong> <code>bdd5e2bf-c6fa-43e6-a5ac-6878fcf814d6</code></li>
<li><strong>Data Type:</strong> <code>categorical</code></li>
<li><strong>Aliases:</strong> enriched cell source barcode name</li>
<li><strong>Subsets:</strong> alignment</li>
</ul>
<p>Name of molecular barcode used to individual Enriched Cell Source to allow for pooling of Enriched Cell Sources before 10x load (Barcoding Cell step) [aka 1st round barcodes]</p>
<p><strong>Permissible values:</strong> <code>Yes</code></p>
</div>

<div id="project-identifier" class="field-detail">
<h5><code>project identifier</code> <em>(required)</em></h5>
<ul>
<li><strong>BICAN UUID:</strong> <code>9a55368b-3b12-47f3-a3cb-ee282c6d73ce</code></li>
<li><strong>Data Type:</strong> <code>integer</code></li>
</ul>
<p>NIMP database id for the project his Enriched Cell Sample is associated with</p>
</div>

<div id="enrichment-population" class="field-detail">
<h5><code>enrichment population</code> <em>(optional)</em></h5>
<ul>
<li><strong>BICAN UUID:</strong> <code>875f1c70-f5aa-45e3-94b9-5e482f6c4830</code></li>
<li><strong>Data Type:</strong> <code>text</code></li>
<li><strong>Subsets:</strong> analysis</li>
</ul>
<p>Actual percentage of cells as a result of using set of fluorescent marker label(s) to enrich dissociated_cell_sample with desired mix of cell populations. This plan can also be used to describe &#x27;No FACS&#x27; where no enrichment was performed. This is a property of enriched_cell_prep_container.</p>
</div>

<div id="histone-modification-marker" class="field-detail">
<h5><code>histone modification marker</code> <em>(optional)</em></h5>
<ul>
<li><strong>BICAN UUID:</strong> <code>a2ef2228-e438-4260-95e5-22eb3b35b5a9</code></li>
<li><strong>Data Type:</strong> <code>text</code></li>
</ul>
<p>Histone modification marker antibodies (eg H3K27ac; H3K27me3; H3K9me3) used in conjunction with an Enriched Cell Source Barcode in order to combine multiple Enriched Cell Populations before Barcoded Cell Sample step for 10xMultiome method. Each of the Histone antibodies captures an essential part of the epigenome.</p>
</div>

<div id="enriched-cell-sample-project" class="field-detail">
<h5><code>enriched cell sample project</code> <em>(required)</em></h5>
<ul>
<li><strong>BICAN UUID:</strong> <code>f59d224e-7732-4409-afb9-a9f502d0173b</code></li>
<li><strong>Data Type:</strong> <code>categorical</code></li>
</ul>
<p>Enriched Cell Sample Project</p>
<p><strong>Permissible values:</strong> <code>Yes</code></p>
</div>

<div id="enriched-cell-sample-lab" class="field-detail">
<h5><code>enriched cell sample lab</code> <em>(required)</em></h5>
<ul>
<li><strong>BICAN UUID:</strong> <code>210cc89d-3b30-4d24-b870-3fa35fe64c2b</code></li>
<li><strong>Data Type:</strong> <code>categorical</code></li>
</ul>
<p>Enriched Cell Sample Lab</p>
<p><strong>Permissible values:</strong> <code>Yes</code></p>
</div>

#### Library

<div id="library-nhash-id" class="field-detail">
<h5><code>library NHash ID</code> <em>(required)</em></h5>
<ul>
<li><strong>BICAN UUID:</strong> <code>f9466382-60f1-45ab-a107-c247531ff3dd</code></li>
<li><strong>Data Type:</strong> <code>text</code></li>
</ul>
<p>NIMP generated globally unique identifier for a Library</p>
</div>

<div id="library-technique" class="field-detail">
<h5><code>library technique</code> <em>(required)</em></h5>
<ul>
<li><strong>BICAN UUID:</strong> <code>7b60d59e-fdd7-4b27-a2d4-cae9b69103a6</code></li>
<li><strong>Data Type:</strong> <code>categorical</code></li>
<li><strong>Aliases:</strong> library method; library chemistry method</li>
<li><strong>Subsets:</strong> analysis; tracking; alignment</li>
</ul>
<p>Standardized nomenclature to describe the library method used. This specifies the alignment method required for the library. For example 10xV3.1 (for RNASeq single assay); 10xMult-GEX (for RNASeq multiome assay); 10xMult-ATAC (for ATACSeq multiome assay).</p>
<p><strong>Permissible values:</strong> <code>Yes</code></p>
</div>

<div id="library-r1/r2-index" class="field-detail">
<h5><code>library r1/r2 index</code> <em>(optional)</em></h5>
<ul>
<li><strong>BICAN UUID:</strong> <code>c94b5d8a-e92d-47af-8c0e-ea3b58be4d06</code></li>
<li><strong>Data Type:</strong> <code>categorical</code></li>
<li><strong>Aliases:</strong> R1/R2 index name</li>
<li><strong>Subsets:</strong> analysis; tracking</li>
</ul>
<p>Name of the pair of library indexes used for sequencing. Indexes allow libraries to be pooled together for sequencing. Sequencing output (fastq) are demultiplexed by using the indexes for each library. The name will be associated with the sequences of i7; i5; and i5as that are needed by SeqCores for demultiplexing. The required direction of the sequence (sense or antisense) of the index can differ depending on sequencing instruments.</p>
<p><strong>Permissible values:</strong> <code>Yes</code></p>
</div>

<div id="library-source-type" class="field-detail">
<h5><code>library source type</code> <em>(optional)</em></h5>
<ul>
<li><strong>BICAN UUID:</strong> <code>5ce18f3d-0e4a-4843-aac6-2b8d3af51c87</code></li>
<li><strong>Data Type:</strong> <code>categorical</code></li>
</ul>
<p>The upstream resource type for library creation. Could be either Barcoded Cell Samples or Amplified cDNA</p>
<p><strong>Permissible values:</strong> <code>Yes</code></p>
</div>

<div id="project-identifier" class="field-detail">
<h5><code>project identifier</code> <em>(required)</em></h5>
<ul>
<li><strong>BICAN UUID:</strong> <code>9a55368b-3b12-47f3-a3cb-ee282c6d73ce</code></li>
<li><strong>Data Type:</strong> <code>integer</code></li>
</ul>
<p>NIMP database id for the project this Library is associated with</p>
</div>

<div id="library-avg-size-bp" class="field-detail">
<h5><code>library avg size bp</code> <em>(optional)</em></h5>
<ul>
<li><strong>BICAN UUID:</strong> <code>f851eba9-56d1-4472-9d0c-d7f8bc33000a</code></li>
<li><strong>Data Type:</strong> <code>integer</code></li>
<li><strong>Subsets:</strong> analysis</li>
<li><strong>Range:</strong> 0 – —</li>
</ul>
<p>Average size of the library in terms of base pairs. This is used to calculate the molarity before pooling and sequencing.</p>
</div>

<div id="library-concentration-nm" class="field-detail">
<h5><code>library concentration nm</code> <em>(optional)</em></h5>
<ul>
<li><strong>BICAN UUID:</strong> <code>90805b3f-f380-4f23-b159-e7eaa0c8f052</code></li>
<li><strong>Data Type:</strong> <code>float</code></li>
<li><strong>Range:</strong> 0 – —</li>
</ul>
<p>Concentration of library in terms of nM (nMol/L). Number of molecules is needed for accurate pooling of the libraries and for generating the number of target reads/cell in sequencing.</p>
</div>

<div id="library-input-ng" class="field-detail">
<h5><code>library input ng</code> <em>(optional)</em></h5>
<ul>
<li><strong>BICAN UUID:</strong> <code>e4d31d97-722d-4771-a0e4-e6062190f2c1</code></li>
<li><strong>Data Type:</strong> <code>float</code></li>
<li><strong>Subsets:</strong> analysis</li>
<li><strong>Range:</strong> 0 – —</li>
</ul>
<p>Amount of cDNA going into library construction in nanograms.</p>
</div>

<div id="library-prep-pass-fail" class="field-detail">
<h5><code>library prep pass-fail</code> <em>(optional)</em></h5>
<ul>
<li><strong>BICAN UUID:</strong> <code>6817ede2-7ead-402d-9dbc-131aca627c6c</code></li>
<li><strong>Data Type:</strong> <code>categorical</code></li>
<li><strong>Aliases:</strong> library prep pass-fail result</li>
<li><strong>Subsets:</strong> analysis</li>
</ul>
<p>Pass or Fail result based on qualitative assessment of library yield and size.</p>
<p><strong>Permissible values:</strong> <code>Yes</code></p>
</div>

<div id="library-quantification-fmol" class="field-detail">
<h5><code>library quantification fmol</code> <em>(optional)</em></h5>
<ul>
<li><strong>BICAN UUID:</strong> <code>4c09ada7-c116-48bc-8fb1-0dcf5c4b939a</code></li>
<li><strong>Data Type:</strong> <code>float</code></li>
<li><strong>Subsets:</strong> analysis</li>
<li><strong>Range:</strong> 0 – —</li>
</ul>
<p>Amount of library generated in terms of femtomoles</p>
</div>

<div id="library-quantification-ng" class="field-detail">
<h5><code>library quantification ng</code> <em>(optional)</em></h5>
<ul>
<li><strong>BICAN UUID:</strong> <code>318b2d3a-dae7-4c63-bfbb-93862b92f63e</code></li>
<li><strong>Data Type:</strong> <code>float</code></li>
<li><strong>Range:</strong> 0 – —</li>
</ul>
<p>Amount of library generated in terms of nanograms</p>
</div>

<div id="library-project" class="field-detail">
<h5><code>library project</code> <em>(required)</em></h5>
<ul>
<li><strong>BICAN UUID:</strong> <code>eb67d39c-2e42-4123-9ac5-71cb08791de4</code></li>
<li><strong>Data Type:</strong> <code>categorical</code></li>
</ul>
<p>Library Project</p>
<p><strong>Permissible values:</strong> <code>Yes</code></p>
</div>

<div id="library-lab" class="field-detail">
<h5><code>library lab</code> <em>(required)</em></h5>
<ul>
<li><strong>BICAN UUID:</strong> <code>b328bb86-d5de-421e-8b33-fa07fdd30f68</code></li>
<li><strong>Data Type:</strong> <code>categorical</code></li>
</ul>
<p>Library Lab</p>
<p><strong>Permissible values:</strong> <code>Yes</code></p>
</div>

#### Library Aliquot

<div id="library-aliquot-local-name" class="field-detail">
<h5><code>library aliquot local name</code> <em>(required)</em></h5>
<ul>
<li><strong>BICAN UUID:</strong> <code>34191bad-d167-4335-8224-ade897d3728e</code></li>
<li><strong>Data Type:</strong> <code>text</code></li>
<li><strong>Aliases:</strong> library aliquot label</li>
<li><strong>Subsets:</strong> analysis; tracking; alignment</li>
</ul>
<p>One library in the library pool. Each Library_aliquot_name in a library pool will have a unique R1/R2 index to allow for sequencing together then separating the sequencing output by originating library aliquot through the process of demultiplexing. The resulting demultiplexed fastq files will include the library_aliquot_name.</p>
</div>

<div id="library-aliquot-nhash-id" class="field-detail">
<h5><code>library aliquot NHash ID</code> <em>(required)</em></h5>
<ul>
<li><strong>BICAN UUID:</strong> <code>3db64dfd-6576-41de-8235-243691238fb2</code></li>
<li><strong>Data Type:</strong> <code>text</code></li>
</ul>
<p>NIMP generated globally unique identifier for a Library Aliquot. This NHash id is a concatenation of the NHash ids of the corresponding Library and the Library Pool.</p>
</div>

<div id="sequencing-result-date" class="field-detail">
<h5><code>sequencing result date</code> <em>(optional)</em></h5>
<ul>
<li><strong>BICAN UUID:</strong> <code>529393f3-ca97-4726-8a22-b1b2284ab30e</code></li>
<li><strong>Data Type:</strong> <code>date</code></li>
</ul>
<p>The date of sequencing results for the Library Aliquot as reported by the Sequencing Center</p>
</div>

<div id="library-aliquot-sequencing-result-status" class="field-detail">
<h5><code>library aliquot sequencing result status</code> <em>(optional)</em></h5>
<ul>
<li><strong>BICAN UUID:</strong> <code>7d6a2e23-efed-4918-98a8-7b9beca99636</code></li>
<li><strong>Data Type:</strong> <code>categorical</code></li>
</ul>
<p>The status of the sequencing results for the Library Aliquot as reported by the Sequencing Center</p>
<p><strong>Permissible values:</strong> <code>Yes</code></p>
</div>

<div id="fastq-file-alignment-status" class="field-detail">
<h5><code>fastq file alignment status</code> <em>(optional)</em></h5>
<ul>
<li><strong>BICAN UUID:</strong> <code>834a0e66-fd81-4d9c-b379-146372c3a629</code></li>
<li><strong>Data Type:</strong> <code>categorical</code></li>
<li><strong>Subsets:</strong> alignment</li>
</ul>
<p>The FASTQ file alignment status as reported by the Library Lab</p>
<p><strong>Permissible values:</strong> <code>Yes</code></p>
</div>

<div id="library-aliquot-fastq-file-size-in-tb" class="field-detail">
<h5><code>library aliquot fastq file size in TB</code> <em>(optional)</em></h5>
<ul>
<li><strong>BICAN UUID:</strong> <code>9ad18a13-465d-44c6-9274-4a2e007150be</code></li>
<li><strong>Data Type:</strong> <code>integer</code></li>
</ul>
<p>Library Aliquot FASTQ File Size in TB</p>
</div>

<div id="library-aliquot-project" class="field-detail">
<h5><code>library aliquot project</code> <em>(required)</em></h5>
<ul>
<li><strong>BICAN UUID:</strong> <code>c972ebc0-bb1f-4124-b69c-8db7b28ef8b7</code></li>
<li><strong>Data Type:</strong> <code>categorical</code></li>
</ul>
<p>Library Aliquot Project</p>
<p><strong>Permissible values:</strong> <code>Yes</code></p>
</div>

<div id="library-aliquot-lab" class="field-detail">
<h5><code>library aliquot lab</code> <em>(required)</em></h5>
<ul>
<li><strong>BICAN UUID:</strong> <code>1c4ca594-b465-4bc9-be3b-2da4f2fce4ea</code></li>
<li><strong>Data Type:</strong> <code>categorical</code></li>
</ul>
<p>Library Aliquot Lab</p>
<p><strong>Permissible values:</strong> <code>Yes</code></p>
</div>

<div id="alignment-qc-status" class="field-detail">
<h5><code>alignment QC status</code> <em>(optional)</em></h5>
<ul>
<li><strong>BICAN UUID:</strong> <code>83dcf584-00c8-48a2-8bda-c360100e7cb3</code></li>
<li><strong>Data Type:</strong> <code>categorical</code></li>
</ul>
<p>Library Aliquot Alignment QC Status</p>
<p><strong>Permissible values:</strong> <code>Yes</code></p>
</div>

<div id="nemo-aliquot-fastq-public-url" class="field-detail">
<h5><code>NeMO aliquot fastq public URL</code> <em>(optional)</em></h5>
<ul>
<li><strong>BICAN UUID:</strong> <code>4c24ea68-c861-4329-9fbd-179de9c63444</code></li>
<li><strong>Data Type:</strong> <code>text</code></li>
</ul>
<p>NeMO Aliquot Fastq Public URL</p>
</div>

<div id="nemo-aliquot-fastq-gcp-url" class="field-detail">
<h5><code>NeMO aliquot fastq gcp URL</code> <em>(optional)</em></h5>
<ul>
<li><strong>BICAN UUID:</strong> <code>7e4711cd-641c-4d8b-9431-8c00c3c56fc5</code></li>
<li><strong>Data Type:</strong> <code>text</code></li>
</ul>
<p>NeMO Aliquot Fastq GCP URL</p>
</div>

<div id="aliquot-alignment-job-id" class="field-detail">
<h5><code>aliquot alignment job ID</code> <em>(optional)</em></h5>
<ul>
<li><strong>BICAN UUID:</strong> <code>7ab5aa8f-297a-4471-9ddd-291a3bbbce0c</code></li>
<li><strong>Data Type:</strong> <code>text</code></li>
</ul>
<p>Library Aliquot Alignment QC Job ID</p>
</div>

<div id="library-aliquot-qc-last-updated-date" class="field-detail">
<h5><code>library aliquot QC last updated date</code> <em>(optional)</em></h5>
<ul>
<li><strong>BICAN UUID:</strong> <code>61a19053-9b68-43b5-ab8c-3d620f3233b7</code></li>
<li><strong>Data Type:</strong> <code>date</code></li>
</ul>
<p>Library Aliquot QC last updated date</p>
</div>

<div id="aliquot-alignment-qc-uploaded-date" class="field-detail">
<h5><code>aliquot alignment QC uploaded date</code> <em>(optional)</em></h5>
<ul>
<li><strong>BICAN UUID:</strong> <code>c0509f07-e68a-49cf-90a4-19be987302ff</code></li>
<li><strong>Data Type:</strong> <code>date</code></li>
</ul>
<p>Library Aliquot alignment QC uploaded date</p>
</div>

<div id="aliquot-qc-total-reads" class="field-detail">
<h5><code>aliquot QC total reads</code> <em>(optional)</em></h5>
<ul>
<li><strong>BICAN UUID:</strong> <code>33a3e1e3-9fc1-45bd-95ee-6649d64dbfbe</code></li>
<li><strong>Data Type:</strong> <code>integer</code></li>
</ul>
<p>Library Aliquot QC total reads</p>
</div>

#### Library Package

<div id="sequencing-center-id" class="field-detail">
<h5><code>sequencing center ID</code> <em>(required)</em></h5>
<ul>
<li><strong>BICAN UUID:</strong> <code>ea95bdad-a450-464f-ac5f-b707be243342</code></li>
<li><strong>Data Type:</strong> <code>categorical</code></li>
</ul>
<p>NIMP id for the Sequencing Center this Library Package will be sent to.</p>
<p><strong>Permissible values:</strong> <code>Yes</code></p>
</div>

#### Library Pool

<div id="library-pool-nhash-id" class="field-detail">
<h5><code>library pool NHash ID</code> <em>(required)</em></h5>
<ul>
<li><strong>BICAN UUID:</strong> <code>9dfdce26-643a-4e1d-8d47-8f418628c893</code></li>
<li><strong>Data Type:</strong> <code>text</code></li>
</ul>
<p>NIMP generated globally unique identifier for a Library Pool</p>
</div>

<div id="library-pool-tube-barcode" class="field-detail">
<h5><code>library pool tube barcode</code> <em>(optional)</em></h5>
<ul>
<li><strong>BICAN UUID:</strong> <code>da02a0ee-9abf-45ef-abb1-981f1aaba6b2</code></li>
<li><strong>Data Type:</strong> <code>text</code></li>
<li><strong>Aliases:</strong> SeqCore library pool tube barcode</li>
<li><strong>Subsets:</strong> analysis; tracking</li>
</ul>
<p>Library Pool tube name as provided by the SeqCore (often a barcode). This tube is provided from the SeqCore and is part of the SeqCore tracking system.</p>
</div>

<div id="flowcell" class="field-detail">
<h5><code>flowcell</code> <em>(optional)</em></h5>
<ul>
<li><strong>BICAN UUID:</strong> <code>4c8d7ac8-d3e3-4177-a93d-18ec2302c392</code></li>
<li><strong>Data Type:</strong> <code>text</code></li>
</ul>
<p>The Flowcell is a unique identifer of the sequencing cartridge (provided by the sequencing instrument manufacturer) used and consumed when sequencing Library Pools on an Illumina sequencing instrument.  A flowcell can be different sizes with different number of lanes.  The flowcell size determines the number of total reads it will produce.  Typically one Flowcell is used to run one Library Pool across all lanes.  Multiple pools can be run on a single flowcell as long as the pools are partitioned onto separate lanes of the flowcell.  Each lane from a flowcell will produce fastq files for all Library Aliquots within the Library Pool applied to a given lane.</p>
</div>

<div id="library-pool-alignment-status" class="field-detail">
<h5><code>library pool alignment status</code> <em>(optional)</em></h5>
<ul>
<li><strong>BICAN UUID:</strong> <code>1b163e8d-fb02-4f95-be76-f72f8fae0a04</code></li>
<li><strong>Data Type:</strong> <code>categorical</code></li>
</ul>
<p>Whether the Library Pool is approved for alignment or not</p>
<p><strong>Permissible values:</strong> <code>Yes</code></p>
</div>

<div id="library-pool-sequencing-instrument" class="field-detail">
<h5><code>library pool sequencing instrument</code> <em>(optional)</em></h5>
<ul>
<li><strong>BICAN UUID:</strong> <code>26b2d0c6-6e01-4238-8992-e138a8d9970c</code></li>
<li><strong>Data Type:</strong> <code>categorical</code></li>
</ul>
<p>Library Pool Sequencing Instrument</p>
<p><strong>Permissible values:</strong> <code>Yes</code></p>
</div>

<div id="library-pool-flowcell-type" class="field-detail">
<h5><code>library pool flowcell type</code> <em>(optional)</em></h5>
<ul>
<li><strong>BICAN UUID:</strong> <code>4b17b73a-ab3c-46c2-81ff-d32da499bccd</code></li>
<li><strong>Data Type:</strong> <code>categorical</code></li>
</ul>
<p>Library Pool Flowcell Type</p>
<p><strong>Permissible values:</strong> <code>Yes</code></p>
</div>

<div id="library-pool-fastq-submission-id" class="field-detail">
<h5><code>library pool fastq submission ID</code> <em>(optional)</em></h5>
<ul>
<li><strong>BICAN UUID:</strong> <code>a314a71c-d68a-4da0-9829-0d64c5087b89</code></li>
<li><strong>Data Type:</strong> <code>text</code></li>
</ul>
<p>Library Pool FASTQ Submission ID</p>
</div>

<div id="library-pool-projects" class="field-detail">
<h5><code>library pool projects</code> <em>(required)</em></h5>
<ul>
<li><strong>BICAN UUID:</strong> <code>b13d9d14-d825-4b50-b20f-716c88ae03ee</code></li>
<li><strong>Data Type:</strong> <code>categorical</code></li>
</ul>
<p>Library Pool Projects</p>
<p><strong>Permissible values:</strong> <code>Yes</code></p>
</div>

<div id="library-pool-labs" class="field-detail">
<h5><code>library pool labs</code> <em>(required)</em></h5>
<ul>
<li><strong>BICAN UUID:</strong> <code>24b59a2a-d841-48b3-b251-4e6210417c4a</code></li>
<li><strong>Data Type:</strong> <code>categorical</code></li>
</ul>
<p>Library Pool Labs</p>
<p><strong>Permissible values:</strong> <code>Yes</code></p>
</div>

<div id="nemo-pool-bucket" class="field-detail">
<h5><code>NeMO pool bucket</code> <em>(optional)</em></h5>
<ul>
<li><strong>BICAN UUID:</strong> <code>eb042898-2e7a-49d8-8378-6fe87aceb80c</code></li>
<li><strong>Data Type:</strong> <code>text</code></li>
</ul>
<p>Nemo Pool Bucket</p>
</div>

#### The LINKML class or data entity (e.g. purple or orange box in the workflow diagram) with which this metadata field is associated

<div id="name-of-metadata-field" class="field-detail">
<h5><code>Name of metadata field</code> <em>(optional)</em></h5>
<ul>
<li><strong>BICAN UUID:</strong> <code>UUID of field in BICAN Ecosystem</code></li>
<li><strong>Data Type:</strong> <code>Type of values in this field (integer; float; text; date)</code></li>
<li><strong>Aliases:</strong> Aliases for this metadata element in other schemas/resources</li>
<li><strong>Subsets:</strong> Data use subset for this field</li>
<li><strong>Range:</strong> For measurements if applicable – For measurements if applicable For measurements if applicable</li>
</ul>
<p>A detailed definition for this field</p>
<p><strong>Permissible values:</strong> <code>For fields that have values from a limited set; see Controlled Values table for entries</code></p>
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

