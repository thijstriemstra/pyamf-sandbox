<cfcomponent>
 	<cffunction name="getCategories" access="remote" returntype="query">
      <cfquery name="results" datasource="customerInfo" dbtype="odbc">select * from categories</cfquery>
      <cfreturn results>
 	</cffunction>
	
 	<cffunction name="getCustomers" access="remote" returntype="query">
 	  <cfargument name="catID" required="true" type="string">
      <cfquery name="results" datasource="customerInfo" dbtype="odbc">select ID, Name, Logo, Details, Active, CategoryID, TotalSales from customerInfo where CategoryID='#catID#'</cfquery>
      <cfreturn results>
 	</cffunction>
</cfcomponent>