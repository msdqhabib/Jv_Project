$(document).ready(function() {
    // Initialize DataTable
    var datatable = $("#datatable").DataTable({
        language: {
            paginate: {
                previous: "<i class='mdi mdi-chevron-left'>",
                next: "<i class='mdi mdi-chevron-right'>"
            }
        },
        drawCallback: function() {
            $(".dataTables_paginate > .pagination").addClass("pagination-rounded");
            $(".dataTables_length select").addClass("form-select form-select-sm");
        }
    });

    // Add the dropdown to the DataTable's controls area
    $("#datatable_filter").append(`
        <label style="margin-left: 10px;">
            Filter: 
            <select id="filter-dropdown" class="form-select form-select-sm" style="display: inline-block; width: auto; margin-left: 5px;">
                <option value="all">All</option>
                <option value="DHA Islamabad-Rawalpindi">DHA Islamabad-Rawalpindi</option>
                <option value="DHA Karachi">DHA Karachi</option>
                <option value="DHA City Karachi">DHA City Karachi</option>
                <option value="SEZ Karachi">SEZ Karachi</option>
                <option value="DHA Bahawalpur">DHA Bahawalpur</option>
                <option value="DHA Lahore">DHA Lahore</option>
                <option value="DHA Quetta">DHA Quetta</option>
                <option value="DHA Gujranwala">DHA Gujranwala</option>
                <option value="DHA Multan">DHA Multan</option>
                <option value="DHA Peshawar">DHA Peshawar</option>
                <!-- Add more options as needed -->
            </select>
        </label>
    `);

    // Get the current filter value from URL
    var url = new URL(window.location.href);
    var currentFilter = url.searchParams.get('filter');

    // Set the selected option in the dropdown
    if (currentFilter) {
        $('#filter-dropdown').val(currentFilter);
    }
    
    // Handle the dropdown change event
    $('#filter-dropdown').change(function() {
        var selectedValue = $(this).val();
        var url = new URL(window.location.href);
        if (selectedValue === 'all') {
            url.searchParams.delete('filter');
        } else {
            url.searchParams.set('filter', selectedValue);
        }
        window.location.href = url.toString();
    });
});